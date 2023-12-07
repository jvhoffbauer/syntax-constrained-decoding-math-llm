import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, LogitsProcessorList

from toolmode.cfg_decoding import logits_processor, parsing, stopping_criteria


class CfgDecoder:
    def __init__(self, model_name: str, grammar_path="funcqa.lark", device_map="cuda:0"):
        # Load model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, load_in_4bit=True, device_map=device_map)

        # Set up model for generation
        self.model.config.pad_token_id = self.model.config.eos_token_id
        self.tokenizer.pad_token = self.tokenizer.eos_token

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
            temperature=None,
            top_p=0,
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
            temperature=None,
            top_p=0,
            # Stop on first <T>
            stopping_criteria=stopping_criteria.TargetSequencetoppingCriteria(
                target_sequence=target_sequence, prompt=prompt, tokenizer=self.tokenizer
            ),
        )

        output_text = self.tokenizer.batch_decode(output_ids[:, prompt_end_index:], skip_special_tokens=True)
        output_text = output_text[0]

        return output_text

    def generate_interleaving(self, prompt: str, max_new_tokens: int, max_operations: int, use_constrained: bool): 
        
        answer_parts = []
        current_prompt = prompt
        last_result = None

        num_operations = 0
        while num_operations < max_operations:

            # First generate free text. This will stop on the first <T> or when max_new_tokens is reached
            # The answer is the free text up to the first <T>, including the <T>
            free_text = self.generate_free(current_prompt, max_new_tokens)

            # Update the prompt
            current_prompt += free_text

            # Ggenerate constrained text until max_operations is reached or the model stops generating
            constrained_text = self.generate_constrained(current_prompt, max_new_tokens)

            # Extract the operation: After the last <T>, excluding the (last) "="
            operation = result.split("<T>")[-1].replace("=", "")

            # Evaluate the constrained text (as it is a formula)
            result = funcqa_runner.evaluate_toolcall(operation)

            # Add the constrained text to the prompt
            current_prompt += constrained_text + "=" + result

            answer_parts += [
                ("free", free_text),
                ("constrained", constrained_text),
                ("result", result),
            ]

            num_operations += 1
            last_result = result

        

            


            

