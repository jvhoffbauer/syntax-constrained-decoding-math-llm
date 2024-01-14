import math
import os

import torch
import inspect
from tqdm import tqdm
import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer, LogitsProcessorList
from toolmode.cfg_decoding import CfgDecoder
from toolmode.data.funcqa import load
from toolmode.prompt import create_prompt
from toolmode.train import get_quantization_kwargs
from peft import LoraConfig, PeftModel


class RunReport:
    """Helper class to easily save a run result."""

    def __init__(self, output_dir, config):
        self.output_dir = output_dir
        self.log_top = ""
        self.log = ""

        self.print_top(f"Run Report: {output_dir}")
        self.print_top()
        self.print_top(f"Config: ")
        for key, value in config.__dict__.items():
            self.print_top(f"  {key}: {value}")
        self.print_top()

    def print_top(self, s: str = ""):
        print(s)
        self.log_top += s + "\n"

    def print(self, s: str = ""):
        print(s)
        self.log += s + "\n"

    def save(self):
        text = self.log_top + "\n\n---------------\n\n" + self.log

        os.makedirs(self.output_dir, exist_ok=True)
        with open(os.path.join(self.output_dir, "report.txt"), "w") as f:
            f.write(text)


BATCH_SIZE = 1


def main():
    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", type=str)
    parser.add_argument("--model_name", type=str)
    parser.add_argument("--adapter_name", type=str, default=None)
    parser.add_argument("--do_not_use_constained", default=False, action="store_true")
    parser.add_argument("--quantization", type=str, default="none")
    parser.add_argument("--use_chat_template", action="store_true", default=False)
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--sanity_check", action="store_true", default=False)
    args = parser.parse_args()

    # Create report
    report = RunReport(args.output_dir, args)

    # Load data
    data = load()["test"]
    if args.sanity_check:
        data = data.select(range(2))

    # Load model
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name, device_map=args.device, **get_quantization_kwargs(args.quantization)
    )
    model.config.pad_token_id = model.config.eos_token_id
    tokenizer.pad_token = tokenizer.eos_token

    # Load adapter if exists
    if args.adapter_name is not None:
        model_merged = PeftModel.from_pretrained(
            model,
            args.adapter_name,
        )
        model = model_merged.merge_and_unload()

    # Create decoder
    decoder = CfgDecoder(model, tokenizer)

    # Batch data
    batches = [data[i : i + BATCH_SIZE] for i in range(0, len(data), BATCH_SIZE)]

    # Generate
    is_correct_all = []
    for batch in tqdm(batches):
        questions = batch["question"]
        prompts = [create_prompt(q, tokenizer=tokenizer, use_chat_template=args.use_chat_template) for q in questions]
        results = decoder.generate_interleaving(
            prompts,
            max_new_tokens_thinking=200,
            max_new_tokens_operation=50,
            use_constrained=not args.do_not_use_constained,
        )
        results_float = [float(r.result) if r.result is not None else float("nan") for r in results]
        is_correct = [
            math.isclose(res, answer, abs_tol=0.1, rel_tol=0.1)
            for res, answer in zip(results_float, batch["answer_number"])
        ]

        report.print(f"Question: {questions}")
        report.print(f"Answers: {[r.to_sentence() for r in results]}")
        report.print(f"Result Numbers: {results_float}")
        report.print(f"Correct Answer: {batch['answer_number']}")
        report.print(f"Is correct: {is_correct}")
        report.print("-" * 80)
        report.print()

        is_correct_all += is_correct
        report.print(f"Accuracy until now: { sum([1 for r in is_correct_all if r]) / len(is_correct_all)}")
        report.print(str(is_correct_all))

    report.print_top(f"Accuracy: {sum([1 for r in is_correct_all if r]) / len(is_correct_all)}")
    report.save()


if __name__ == "__main__":
    main()
