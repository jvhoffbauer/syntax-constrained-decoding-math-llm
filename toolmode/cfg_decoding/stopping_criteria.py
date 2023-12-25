from transformers import StoppingCriteria


class TargetSequencetoppingCriteria(StoppingCriteria):
    def __init__(self, target_sequence, prompts, tokenizer):
        self.target_sequence = target_sequence
        self.prompts = prompts
        self.tokenizer = tokenizer

    def __call__(self, input_ids, scores, **kwargs):
        # Get the generated text as a string
        generated_texts = self.tokenizer.batch_decode(input_ids, skip_special_tokens=True)
        generated_texts = [t.replace(p, "") for t, p in zip(generated_texts, self.prompts)]

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
