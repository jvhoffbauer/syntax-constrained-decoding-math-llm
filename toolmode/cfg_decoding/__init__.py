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

    def to_sentence(self):
        return "".join([str(step.text) for step in self.steps])


class CfgDecoder:
    def __init__(self, model, tokenizer, grammar_path="funcqa.lark", device_map="cuda:0"):
        self.model = model
        self.tokenizer = tokenizer

        # Load grammar
        with open(grammar_path, "r") as f:
            self.grammar_definition = f.read()
        self.parsing_stepper = parsing.create_parsing_stepper(self.grammar_definition, self.tokenizer)

    def generate(
        self,
        prompts: str,
        max_new_tokens: int,
        mask: List[bool],
        use_constrained: bool,
        target_sequence: str | None = None,
    ):
        """
        Will skip prompts where mask is False
        """
        # Filter prompts that are not masked
        prompts = [prompt for m, prompt in zip(mask, prompts) if m]

        # Create input ids
        input_ids = self.tokenizer(prompts, return_tensors="pt", padding=True).input_ids
        input_ids = input_ids.to(self.model.device)

        # Generate
        if use_constrained:
            output_ids = self.model.generate(
                input_ids,
                logits_processor=LogitsProcessorList(
                    [
                        logits_processor.GrammarConstrainedLogitsProcessorGpu(
                            self.tokenizer,
                            torch.ones((len(prompts),)).long().to(self.model.device) * (input_ids.shape[1]),
                            self.model.device,
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
                    target_sequence=target_sequence,
                    prompt_end_indices=torch.ones((len(prompts),)).long().to(self.model.device) * (input_ids.shape[1]),
                    tokenizer=self.tokenizer,
                ),
            )

        # Extract texts from ids
        texts = self.tokenizer.batch_decode(output_ids[:, input_ids.shape[1] :], skip_special_tokens=True)

        # Remove everything after the target sequence
        # This is needed as the model might generate more than the target sequence for the batch indices that hit it first
        if target_sequence is not None:
            texts = [t.split(target_sequence)[0] for t in texts]

        # Reorder texts to match the original order (as some texts might have been skipped)
        texts_full = [""] * len(mask)
        for i, m in enumerate(mask):
            if m:
                texts_full[i] = texts.pop(0)

        return texts_full

    def generate_interleaving(
        self, prompts: List[str], max_new_tokens_thinking: int, max_new_tokens_operation: int, use_constrained: bool
    ) -> GenerationResult:
        """ """
        batch_size = len(prompts)
        current_prompts = prompts
        answer_parts = [[] for _ in prompts]
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
            free_texts = [t + "<T>" if not t.endswith("<T>") else t for t in free_texts]

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
                prompt + op + "=" + str(res) + " " for prompt, op, res in zip(current_prompts, operations, results)
            ]

            # Check if we are done
            for i, result in enumerate(results):
                if is_done[i]:
                    continue
                elif result is None:
                    is_done[i] = True
                elif len(answer_parts[i]) / 3 >= MAX_GENERATION_STEPS:
                    is_done[i] = True
                elif "####" in free_texts[i]:
                    is_done[i] = True

            # Store the answer
            for i, _ in enumerate(answer_parts):
                answer_parts[i].append(GenerationStep("free", free_texts[i]))

                if is_done[i]:
                    continue

                answer_parts[i].append(GenerationStep("constrained" if use_constrained else "free", operation_texts[i]))
                answer_parts[i].append(GenerationStep("operation", results[i]))
                last_results[i] = results[i]

        return [GenerationResult(a, l) for a, l in zip(answer_parts, last_results)]
