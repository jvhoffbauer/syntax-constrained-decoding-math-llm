from transformers import StoppingCriteria


class TargetSequencetoppingCriteria(StoppingCriteria):
    def __init__(self, target_sequence, prompt_end_indices, tokenizer):
        self.target_sequence = target_sequence
        self.prompt_end_indices = prompt_end_indices
        self.tokenizer = tokenizer

    def __call__(self, input_ids, scores, **kwargs):
        if (input_ids.shape[1] == self.prompt_end_indices).all():
            # The prompt is the only thing in the input_ids
            return False

        # Get the generated text as a string
        generated_texts = self.tokenizer.batch_decode(
            input_ids[:, self.prompt_end_indices], skip_special_tokens=False, clean_up_tokenization_spaces=False
        )

        # Check if the target sequence appears in the generated text
        if all(self.target_sequence in t for t in generated_texts):
            # Stop generation
            return True
        else:
            # Continue generation
            return False

    def __len__(self):
        return 1

    def __iter__(self):
        yield self
