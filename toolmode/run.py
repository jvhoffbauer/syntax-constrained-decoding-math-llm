import math

import torch
from tqdm import tqdm
from transformers import (AutoModelForCausalLM, AutoTokenizer,
                          LogitsProcessorList)

from toolmode.cfg_decoding import CfgDecoder
from toolmode.data.funcqa import load

MODEL_NAME = "funcqa_zephyr/merged_model_final"
# MODEL_NAME = "01-ai/Yi-34B-Chat"
# MODEL_NAME = "pankajmathur/orca_mini_3b"
# MODEL_NAME = "01-ai/Yi-6B-Chat"
# MODEL_NAME = "HuggingFaceH4/zephyr-7b-alpha"


def main():
    # Load data
    data = load()

    # Load model
    device_map = "cuda:2"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, load_in_4bit=True, device_map=device_map, torch_dtype=torch.bfloat16)
    model.config.pad_token_id = model.config.eos_token_id
    tokenizer.pad_token = tokenizer.eos_token

    # Create decoder
    decoder = CfgDecoder(model, tokenizer)

    # Generate
    results = []
    for row in tqdm(data):
        prompt = row["prompt"]
        question = row["question"]
        answer = row["answer"]
        num_operations = len(row["calculation"])
        result = decoder.generate_interleaving(
            prompt, max_new_tokens=100, max_operations=num_operations, use_constrained=True
        )
        result_float = float(result.result) if result.result is not None else float("nan")
        is_correct = math.isclose(result_float, answer, rel_tol=0.1)

        print(f"Question: {question}")
        print(f"Correct Answer: {answer}")
        print(f"Given Answer: {result.result}")
        print(f"Correct Operations:" + " | ".join(row["calculation"]))
        print(f"Generated Operations:" + " | ".join([str(o) for o in result.get_generations("constrained")]))
        print(f"Full answer:" + str(result))
        print(f"Is correct: {is_correct}")
        print("-" * 80)
        print()

        results.append(
            {
                "anser_given": result.result,
                "answer_correct": answer,
                "is_correct": is_correct,
            }
        )
        print("Accuracy until now:", sum([1 for r in results if r["is_correct"]]) / len(results))

    print(results)
    print("Accuracy:", sum([1 for r in results if r["is_correct"]]) / len(results))


if __name__ == "__main__":
    main()
