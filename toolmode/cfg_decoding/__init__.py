from dataclasses import dataclass
from typing import Literal

import torch
from transformers import LogitsProcessorList

from toolmode.cfg_decoding import logits_processor, parsing, stopping_criteria
from toolmode.data.funcqa import runner as funcqa_runner


@dataclass
class GenerationStep:
    generation_type: Literal["free", "constrained", "operation"]
    text: str

    def __str__(self):
        return f"{self.generation_type}: {self.text}"


@dataclass
class GenerationResult:
    steps: list[GenerationStep]
    result: float | None

    def __str__(self):
        return f"Result: {self.result}. Steps:" + " | ".join([str(step) for step in self.steps])

    def get_generations(self, generation_type: Literal["free", "constrained", "operation"]):
        return [generation for generation in self.steps if generation.generation_type == generation_type]


class CfgDecoder:
    def __init__(self, model, tokenizer, grammar_path="funcqa.lark", device_map="cuda:0"):
        self.model = model
        self.tokenizer = tokenizer

        # Load grammar
        with open(grammar_path, "r") as f:
            self.grammar_definition = f.read()
        self.parsing_stepper = parsing.create_parsing_stepper(self.grammar_definition, self.tokenizer)

    def generate_constrained(self, prompt: str, max_new_tokens: int):
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        bos_ids = torch.ones((1, 1), dtype=torch.long) * self.model.config.bos_token_id
        input_ids = torch.cat([bos_ids, input_ids], dim=-1)
        input_ids = input_ids.to(self.model.device)

        prompt_end_index = input_ids.shape[1]

        output_ids = self.model.generate(
            input_ids,
            logits_processor=LogitsProcessorList(
                [
                    logits_processor.GrammarConstrainedLogitsProcessor(
                        self.tokenizer, self.parsing_stepper, prompt_end_index=prompt_end_index
                    )
                ]
            ),
            max_new_tokens=max_new_tokens,
            pad_token_id=self.tokenizer.eos_token_id,
            # No sampling
            do_sample=False,
            # temperature=None,
            # top_p=0,
        )

        output_text = self.tokenizer.batch_decode(output_ids[:, prompt_end_index:], skip_special_tokens=True)
        output_text = output_text[0]
        return output_text

    def generate_free(self, prompt: str, max_new_tokens: int, target_sequence: str = "<T>"):
        """
        Generate free text until the target sequence was generated or max_new_tokens is reached
        Return (only) the generated text including the target sequence
        """
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        bos_ids = torch.ones((1, 1), dtype=torch.long) * self.model.config.bos_token_id
        input_ids = torch.cat([bos_ids, input_ids], dim=-1)
        input_ids = input_ids.to(self.model.device)

        prompt_end_index = input_ids.shape[1]

        output_ids = self.model.generate(
            input_ids,
            max_new_tokens=max_new_tokens,
            pad_token_id=self.tokenizer.eos_token_id,
            # No sampling
            do_sample=False,
            # temperature=None,
            # top_p=0,
            # Stop on first <T>
            stopping_criteria=stopping_criteria.TargetSequencetoppingCriteria(
                target_sequence=target_sequence, prompt=prompt, tokenizer=self.tokenizer
            ),
        )

        output_text = self.tokenizer.batch_decode(output_ids[:, prompt_end_index:], skip_special_tokens=True)
        output_text = output_text[0]

        return output_text

    def generate_interleaving(
        self, prompt: str, max_new_tokens: int, max_operations: int, use_constrained: bool
    ) -> GenerationResult:
        answer_parts = []
        current_prompt = prompt
        last_result = -1

        num_operations = 0
        while num_operations < max_operations and last_result is not None:
            # First generate free text. This will stop on the first <T> or when max_new_tokens is reached
            # The answer is the free text up to the first <T>, including the <T>
            free_text = self.generate_free(current_prompt, max_new_tokens)

            # It can happen that the model stops generating before the first <T> is reached
            # In this case, manually add the <T> to the answer
            if not free_text.endswith("<T>"):
                free_text += "<T>"

            # Update the prompt
            current_prompt += free_text

            # Ggenerate constrained text until max_operations is reached or the model stops generating
            if use_constrained:
                operation_text = self.generate_constrained(current_prompt, max_new_tokens)
            else:
                operation_text = self.generate_free(current_prompt, max_new_tokens, target_sequence="=")

            # Extract the operation: After the last <T>, excluding the (last) "="
            operation = operation_text.replace("=", "")

            # Evaluate the constrained text (as it is a formula)
            result = funcqa_runner.evaluate_toolcall(operation)

            # Add the constrained text to the prompt
            current_prompt += operation + "=" + str(result) + " "

            answer_parts += [
                GenerationStep("free", free_text),
                GenerationStep("constrained" if use_constrained else "free", operation_text),
                GenerationStep("operation", result),
            ]

            num_operations += 1
            last_result = result

        return GenerationResult(answer_parts, last_result)
