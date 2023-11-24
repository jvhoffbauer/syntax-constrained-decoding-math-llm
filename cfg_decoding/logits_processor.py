from transformers import LogitsProcessor
import torch


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
        decoded_sequences = self.tokenizer.batch_decode(input_ids[:, self.prompt_end_index:], skip_special_tokens=True)

        # Get parsing states per sequence 
        parsing_states = [self.parsing_stepper.get_parsing_state(seq) for seq in decoded_sequences]

        print("Decoded sequences: ", [d[-10:] for d in decoded_sequences])
        print("Parsing states: ", parsing_states)

        # Part of the current terminal that is already generated
        existing_tokens_for_terminal = [
            seq[state.current_terminal_start_index:]
            for seq, state in zip(decoded_sequences, parsing_states)
        ]
        # list of lists of token ids
        valid_tokens = [
            self._filter_tokens_by_regex(existing_part, self.all_tokens, state.active_terminal_patterns) 
            for state, existing_part in zip(parsing_states, existing_tokens_for_terminal)
        ]
        # list of lists of token ids
        valid_token_ids = [
            self.tokenizer.convert_tokens_to_ids(tokens) 
            for tokens in valid_tokens
        ]  

        print("Existing tokens for terminal: ", existing_tokens_for_terminal)
        print("Valid tokens: ", valid_tokens)

        # Mask out scores 
        scores_mask = torch.ones_like(scores) * float('inf') * -1
        for sequence_index, valid_token_ids_for_sequence in enumerate(valid_token_ids):
            scores_mask[sequence_index, valid_token_ids_for_sequence] = 0

        scores = scores + scores_mask
        
        print("-" * 20)
        return scores
        

    def _filter_tokens_by_regex(self, existing_part, tokens, regexes):
        """
        Filter tokens by regexes
        """
        return [
            token 
            for token in tokens 
            if any(regex.fullmatch(existing_part + token, partial=True) for regex in regexes)
        ]
