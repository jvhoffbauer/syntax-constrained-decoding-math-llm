import copy
from pprint import pprint

import torch
from transformers import LogitsProcessor


class GrammarConstrainedLogitsProcessor(LogitsProcessor):
    def __init__(self, tokenizer, parsing_stepper, prompt_end_index):
        self.tokenizer = tokenizer
        self.all_tokens = self.tokenizer.convert_ids_to_tokens(range(self.tokenizer.vocab_size))
        self.parsing_stepper = parsing_stepper
        self.prompt_end_index = prompt_end_index

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor:
        # input_ids: B * num_beams x T
        # scores: B * num_beams x V

        # Decode sequences
        decoded_sequences = self.tokenizer.batch_decode(input_ids[:, self.prompt_end_index :], skip_special_tokens=True)

        # Get parsing states per sequence
        parsing_states = [self.parsing_stepper.get_parsing_state(seq) for seq in decoded_sequences]

        # print("Decoded sequences: ", [d[-10:] for d in decoded_sequences])
        # print("Parsing states: ", parsing_states)

        # Part of the current terminal that is already generated
        existing_tokens_for_terminal = [
            seq[state.current_terminal_start_index :] for seq, state in zip(decoded_sequences, parsing_states)
        ]
        # list of lists of token ids
        valid_tokens = [
            self._filter_tokens_by_regex(existing_part, self.all_tokens, state.active_terminal_patterns)
            for state, existing_part in zip(parsing_states, existing_tokens_for_terminal)
        ]
        # list of lists of token ids
        valid_token_ids = [self.tokenizer.convert_tokens_to_ids(tokens) for tokens in valid_tokens]

        # print("Existing tokens for terminal: ", existing_tokens_for_terminal)
        # print("Valid tokens: ", valid_tokens)

        # Mask out scores
        scores_mask = torch.ones_like(scores) * float("inf") * -1
        for sequence_index, valid_token_ids_for_sequence in enumerate(valid_token_ids):
            scores_mask[sequence_index, valid_token_ids_for_sequence] = 0

        scores = scores + scores_mask

        # print("-" * 20)
        return scores

    def _filter_tokens_by_regex(self, existing_part, tokens, regexes):
        """
        Filter tokens by regexes
        """
        return [
            token for token in tokens if any(regex.fullmatch(existing_part + token, partial=True) for regex in regexes)
        ]


FSA = {
    "S": {
        "add": "OPEN_BRACKET",
        "subtract": "OPEN_BRACKET",
        "multiply": "OPEN_BRACKET",
        "divide": "OPEN_BRACKET",
        "power": "OPEN_BRACKET",
        "sqrt": "OPEN_BRACKET",
        "log": "OPEN_BRACKET",
        "ln": "OPEN_BRACKET",
        "choose": "OPEN_BRACKET",
        "permutate": "OPEN_BRACKET",
        "gcd": "OPEN_BRACKET",
        "lcm": "OPEN_BRACKET",
        "remainder": "OPEN_BRACKET",
    },
    "OPEN_BRACKET": {
        "(": "NUMBER_P0",
    },
    "NUMBER_P0": {
        "0": "NUMBER_P1",
        "1": "NUMBER_P1",
        "2": "NUMBER_P1",
        "3": "NUMBER_P1",
        "4": "NUMBER_P1",
        "5": "NUMBER_P1",
        "6": "NUMBER_P1",
        "7": "NUMBER_P1",
        "8": "NUMBER_P1",
        "9": "NUMBER_P1",
    },
    "NUMBER_P1": {
        ".": "NUMBER_P2",
        ",": "ARGUMENT_SPACE",
        ")=": "FINAL",
        "0": "NUMBER_P1",
        "1": "NUMBER_P1",
        "2": "NUMBER_P1",
        "3": "NUMBER_P1",
        "4": "NUMBER_P1",
        "5": "NUMBER_P1",
        "6": "NUMBER_P1",
        "7": "NUMBER_P1",
        "8": "NUMBER_P1",
        "9": "NUMBER_P1",
    },
    "NUMBER_P2": {
        ",": "ARGUMENT_SPACE",
        ")=": "FINAL",
        "0": "NUMBER_P2",
        "1": "NUMBER_P2",
        "2": "NUMBER_P2",
        "3": "NUMBER_P2",
        "4": "NUMBER_P2",
        "5": "NUMBER_P2",
        "6": "NUMBER_P2",
        "7": "NUMBER_P2",
        "8": "NUMBER_P2",
        "9": "NUMBER_P2",
    },
    "ARGUMENT_SPACE": {
        " ": "NUMBER_P0",
    },
    "FINAL": {
        "</s>": "FINAL",
    },
}


class FsaGpu:
    def __init__(self, tokenizer, device):
        self.tokenizer = tokenizer
        self.fsa = copy.deepcopy(FSA)

        # First, encode all words in our FSA vocabulary
        # words = {w: tokenizer.encode(w, add_special_tokens=False) for w in WORDS}
        # Now, break down transitions that consume multiple tokens (because the word is longer than one token)
        for state, transitions in list(self.fsa.items()):
            for transition, next_state in list(transitions.items()):
                transition_tokens = self._tokenize(transition)
                if len(transition_tokens) > 1:
                    # Remove existing transition
                    del self.fsa[state][transition]
                    # Add new intermediate transitions that consume one token each
                    self.fsa[state][transition_tokens[0]] = f"{transition}.1.{next_state}"
                    for i, token in list(enumerate(transition_tokens))[1:-1]:
                        self.fsa[f"{transition}.{i}.{next_state}"] = {token: f"{transition}.{i+1}.{next_state}"}
                    # Add final transition that consumes the last token
                    self.fsa[f"{transition}.{len(transition_tokens)-1}.{next_state}"] = {
                        transition_tokens[-1]: next_state
                    }

        # Convert all string transitions to single ids
        for state, transitions in list(self.fsa.items()):
            for transition, next_state in list(transitions.items()):
                del self.fsa[state][transition]
                token_ids = self._encode(transition)
                assert (
                    len(token_ids) == 1
                ), f"Transition {transition} from {state} to {next_state} is not a single token"
                token_id = token_ids[0]
                self.fsa[state][token_id] = next_state

        # Create mapping of state ids
        self.state_ids2state = {i: state for i, state in enumerate(self.fsa.keys())}
        self.state2state_ids = {state: i for i, state in enumerate(self.fsa.keys())}

        # Create tensor from fsa
        self.fsa_tensor = torch.ones((len(self.fsa), self.tokenizer.vocab_size), dtype=torch.int32) * -1
        for state, transitions in self.fsa.items():
            for transition, next_state in transitions.items():
                self.fsa_tensor[self.state2state_ids[state], transition] = self.state2state_ids[next_state]
        self.fsa_tensor = self.fsa_tensor.to(device)

    def _tokenize(self, text):
        """
        Tokenize text and return a list of token ids. Ensures that no extra whitespace is added.
        """
        tokens_prefix = self.tokenizer.tokenize("\n", add_special_tokens=False)
        tokens = self.tokenizer.tokenize("\n" + text, add_special_tokens=False)

        assert (
            tokens[: len(tokens_prefix)] == tokens_prefix
        ), f"Could not tokenize {text}. It was tokenized as {tokens} while the prefix is {tokens_prefix}"

        tokens = tokens[len(tokens_prefix) :]
        return tokens

    def _encode(self, text):
        ids_prefix = self.tokenizer.encode("\n", add_special_tokens=False)
        ids = self.tokenizer.encode("\n" + text, add_special_tokens=False)

        # Remove prefix
        return ids[len(ids_prefix) :]

    def get_token_mask(self, input_ids, start_indices):
        """
        Return a mask of B x |Vocab| that is 1 for each token that can be generated according to the grammar
        """
        B = input_ids.shape[0]

        # First, apply the grammar to the input_ids
        states = torch.ones((B,), dtype=torch.int32, device=input_ids.device) * self.state2state_ids["S"]
        indices = start_indices.clone().to(input_ids.device)
        is_finished = torch.zeros((B,), dtype=torch.bool, device=input_ids.device)

        # Get num steps
        num_steps = input_ids.shape[1] - start_indices
        num_steps = torch.max(num_steps)
        num_steps = num_steps.item()

        # Run the automata until we reach the final state
        for _ in range(num_steps):
            # Get the next tokens
            next_tokens = torch.where(~is_finished, input_ids[torch.arange(B), indices], -1)

            # Get the next states
            next_states = torch.where(~is_finished, self.fsa_tensor[states, next_tokens], states)

            # Update states
            states = next_states

            # Update indices
            indices += 1
            is_finished = indices >= input_ids.shape[1]
            indices = torch.min(indices, torch.ones_like(indices) * (input_ids.shape[1] - 1))

        # Get the enabled tokens for the final states
        mask = self.fsa_tensor[states] != -1
        mask = mask.int()

        return mask, states


class GrammarConstrainedLogitsProcessorGpu(LogitsProcessor):
    def __init__(self, tokenizer, prompt_end_index, device):
        self.tokenizer = tokenizer
        self.prompt_end_index = prompt_end_index
        self.fsa = FsaGpu(tokenizer, device)

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor:
        # input_ids: B * num_beams x T
        # scores: B * num_beams x V

        mask, _ = self.fsa.get_token_mask(input_ids, self.prompt_end_index)
        mask = torch.where(mask == 1, 0, float("-inf"))
        scores = scores + mask
        return scores


def main():
    from transformers import AutoTokenizer

    g = FsaGpu(AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta"))

    input_tokens = torch.Tensor(g._encode("ln(1, 2)=")).long().unsqueeze(0)
    mask, states = g.get_token_mask(input_tokens, torch.tensor([0]))
    tokens = g.tokenizer.convert_ids_to_tokens(torch.where(mask)[1].tolist())
    print(states)
    print(tokens)


if __name__ == "__main__":
    main()
