from dataclasses import dataclass
from typing import List, Literal

import torch
from transformers import LogitsProcessorList

from toolmode.cfg_decoding import logits_processor, parsing, stopping_criteria
from toolmode.data.funcqa import runner as funcqa_runner

MAX_GENERATION_STEPS = 3


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

    def generate(
        self, prompts: str, max_new_tokens: int, mask: List[bool], use_constrained: bool, target_sequence: str = "<T>"
    ):
        """
        Will skip prompts where mask is False
        """
        # Filter prompts that are not masked
        prompts = [prompt for m, prompt in zip(mask, prompts) if mask]

        # Create input ids
        input_ids = self._create_input_ids(prompts)

        # Generate
        if use_constrained:
            output_ids = self.model.generate(
                input_ids,
                logits_processor=LogitsProcessorList(
                    [
                        logits_processor.GrammarConstrainedLogitsProcessor(
                            self.tokenizer, self.parsing_stepper, prompt_end_index=input_ids.shape[1]
                        )
                    ]
                ),
                max_new_tokens=max_new_tokens,
                pad_token_id=self.tokenizer.eos_token_id,
                # No sampling
                do_sample=False,
            )
        else:
            output_ids = self.model.generate(
                input_ids,
                max_new_tokens=max_new_tokens,
                pad_token_id=self.tokenizer.eos_token_id,
                # No sampling
                do_sample=False,
                # Stop on first <T>
                stopping_criteria=stopping_criteria.TargetSequencetoppingCriteria(
                    target_sequence=target_sequence, prompt=prompts, tokenizer=self.tokenizer
                ),
            )

        # Extract texts from ids
        texts = self._get_texts_from_ids(output_ids, input_ids.shape[1])

        # Reorder texts to match the original order (as some texts might have been skipped)
        texts_full = [""] * len(mask)
        for i, m in enumerate(mask):
            if m:
                texts_full[i] = texts.pop(0)

        return texts_full

    def _create_input_ids(self, prompts: List[str]):
        input_ids = self.tokenizer(prompts, return_tensors="pt").input_ids
        bos_ids = torch.ones((len(prompts), 1), dtype=torch.long) * self.model.config.bos_token_id
        input_ids = torch.cat([bos_ids, input_ids], dim=-1)
        input_ids = input_ids.to(self.model.device)
        return input_ids

    def _get_texts_from_ids(self, output_ids, prompt_end_index) -> List[str]:
        output_text = self.tokenizer.batch_decode(output_ids[:, prompt_end_index:], skip_special_tokens=True)
        return output_text

    def generate_interleaving(
        self, prompts: List[str], max_new_tokens_thinking: int, max_new_tokens_operation: int, use_constrained: bool
    ) -> GenerationResult:
        """ """
        batch_size = len(prompts)
        current_prompts = prompts
        answer_parts = [[]] * batch_size
        last_results = [None] * batch_size
        is_done = [False] * batch_size

        while any(not done for done in is_done):
            # First generate free text. This will stop on the first <T> or when max_new_tokens is reached
            # The answer is the free text up to the first <T>, including the <T>
            free_texts = self.generate(
                prompts=current_prompts,
                max_new_tokens=max_new_tokens_thinking,
                use_constrained=False,
                target_sequence="<T>",
                mask=[not done for done in is_done],
            )

            # It can happen that the model stops generating before the first <T> is reached
            # In this case, manually add the <T> to the answer
            free_texts = [t + "<T>" if t.endswith("<T>") else t for t in free_texts]

            # Update the prompt
            current_prompts = [p + t for p, t in zip(current_prompts, free_texts)]

            # Generate constrained text until max_operations is reached or the model stops generating
            if use_constrained:
                operation_texts = self.generate(
                    prompts=current_prompts,
                    max_new_tokens=max_new_tokens_operation,
                    use_constrained=True,
                    mask=[not done for done in is_done],
                )
            else:
                operation_texts = self.generate(
                    prompts=current_prompts,
                    max_new_tokens=max_new_tokens_operation,
                    target_sequence="=",
                    use_constrained=False,
                    mask=[not done for done in is_done],
                )

            # Extract the operation: After the last <T>, excluding the (last) "="
            operations = [o.replace("=", "") for o in operation_texts]

            # Evaluate the constrained text (as it is a formula)
            results = [funcqa_runner.evaluate_toolcall(o) for o in operations]

            # Add the constrained text to the prompt
            current_prompts = [
                prompt + op + "=" + res + " " for prompt, op, res in zip(current_prompts, operation_texts, results)
            ]

            # Store the answer
            for i, _ in enumerate(answer_parts):
                if is_done[i]:
                    continue
                answer_parts[i] += [
                    GenerationStep("free", free_texts[i]),
                    GenerationStep("constrained" if use_constrained else "free", operation_texts[i]),
                    GenerationStep("operation", results[i]),
                ]
                last_results[i] = results[i]

            # Check if we are done
            for i, result in enumerate(results):
                if is_done[i]:
                    continue
                elif result is None:
                    is_done[i] = True
                elif len(answer_parts[i] / 3) >= MAX_GENERATION_STEPS:
                    is_done[i] = True
                elif free_texts[i] in ["", "."]:
                    is_done[i] = True

        return [GenerationResult(a, l) for a, l in zip(answer_parts, last_results)]
