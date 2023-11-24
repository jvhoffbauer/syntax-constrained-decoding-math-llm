from transformers import LogitsProcessor
import torch


class LogitsProcessor(LogitsProcessor):
    def __init__(self, tokenizer, parsing_stepper):
        self.tokenizer = tokenizer
        self.all_tokens = self.tokenizer.convert_ids_to_tokens(range(self.tokenizer.vocab_size))
        self.parsing_stepper = parsing_stepper

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor:

        # input_ids: B * num_beams x T
        # scores: B * num_beams x V

        # Decode sequences
        decoded_sequences = self.tokenizer.batch_decode(input_ids, skip_special_tokens=True)

        # Get parsing states per sequence 
        parsing_states = [self.parsing_stepper.get_parsing_state(seq) for seq in decoded_sequences]

        valid_tokens = [self._filter_tokens_by_regex(self.all_tokens, state.active_terminal_patterns) for state in parsing_states]
        valid_token_ids = [self.tokenizer.convert_tokens_to_ids(tokens) for tokens in valid_tokens]  # list of lists of token ids

        # Mask out scores 
        scores_mask = torch.ones_like(scores) * float('inf') * -1
        for sequence_index, valid_token_ids_for_sequence in enumerate(valid_token_ids):
            scores_mask[sequence_index, valid_token_ids_for_sequence] = 0

        scores = scores + scores_mask
        
        return scores
        

    def _filter_tokens_by_regex(self, tokens, regexes):
        """
        Filter tokens by regexes
        """
        return [
            token 
            for token in tokens 
            if any(regex.fullmatch(token, partial=True) for regex in regexes)
        ]
