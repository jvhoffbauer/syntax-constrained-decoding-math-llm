import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, LogitsProcessorList

import cfg_decoding.logits_processor as lp
import cfg_decoding.parsing as p


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
        self.parsing_stepper = p.create_parsing_stepper(self.grammar_definition, self.tokenizer)

    def generate(self, prompt: str, max_new_tokens: int):
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        input_ids = input_ids.unsqueeze(0)
        bos_ids = torch.ones((1,), dtype=torch.long) * self.model.config.bos_token_id
        input_ids = torch.cat([bos_ids, input_ids], dim=-1)
        input_ids = input_ids.to(self.model.device)

        prompt_end_index = input_ids.shape[1]

        output_ids = self.model.generate(
            input_ids,
            logits_processor=LogitsProcessorList(
                [
                    lp.GrammarConstrainedLogitsProcessor(
                        self.tokenizer, self.parsing_stepper, prompt_end_index=prompt_end_index
                    )
                ]
            ),
            max_new_tokens=max_new_tokens,
            pad_token_id=self.tokenizer.eos_token_id,
            # No sampling
            do_sample=False,
            temperature=0.0,
        )

        output_text = self.tokenizer.batch_decode(output_ids[:, prompt_end_index:], skip_special_tokens=True)
        output_text = output_text[0]
        return output_text
