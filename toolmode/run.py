import math

import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer, LogitsProcessorList

from toolmode.cfg_decoding import CfgDecoder
from toolmode.data.funcqa import load

# MODEL_NAME = "funcqa_zephyr/merged_model_final"
# MODEL_NAME = "meta-llama/Llama-2-13b-chat-hf"
# MODEL_NAME = "pankajmathur/orca_mini_3b"
# MODEL_NAME = "01-ai/Yi-34B-Chat"
# MODEL_NAME = "HuggingFaceH4/zephyr-7b-beta"
MODEL_NAME = "funcqa_zephyr_e1/merged_model_final"


BATCH_SIZE = 1
USE_CHAT_TEMPLATE = False

CUDA_DEVICE_ID = 0


def create_prompt(question, use_chat_template, tokenizer=None):
    if use_chat_template:
        prompt = tokenizer.apply_chat_template(
            [
                {
                    "role": "system",
                    "content": "You are a helpful chatbot. You answer the following question using toolcalls to the tools: add, subtract, multiply, divide, power, sqrt, log, lcm, gcd, ln, choose, remainder, and permutate. You initiate the toolmode with the token <T>. You answer only the question the user provides you. End every answer with ####",
                },
                {
                    "role": "user",
                    "content": "A coin is tossed 8 times, what is the probability of getting exactly 7 heads ?",
                },
                {
                    "role": "assistant",
                    "content": "The total number of possible outcomes to toss a coin 8 times is 2^8=<T>power(2,8)=256. The number of ways of getting exactly 7 heads is 8C7=<T>choose(8,7)=8. The probability of getting exactly 7 heads is 8/256=<T>divide(8,256)=0.03125. ####",
                },
                {
                    "role": "user",
                    "content": "If paint costs $3.2 per quart, and a quart covers 12 square feet, how much will it cost to paint the outside of a cube 10 feet on each edge?",
                },
                {
                    "role": "assistant",
                    "content": "The total surface area of the 10 ft cube is 6*10^2=6*<T>power(10,2)=100=<T>multiply(6,100)=600 square feet. The number of quarts needed is 600/12=<T>divide(600,12)=50. The cost is 50*3.2=<T>multiply(50,3.2)=160. ####",
                },
                {
                    "role": "user",
                    "content": "log(x)=2, log(y)=0.1, what is the value of log(x-y) ?",
                },
                {
                    "role": "assistant",
                    "content": "log(x)=2, so x=10^2=<T>power(10,2)=100; log(y)=0.1, so y=10^0.1=<T>power(10,0.1)=1.26; x-y=100-1.26=<T>subtract(10,1.26)=98.74, so log(x-y)=log(98.74)=<T>log(98.74)=1.99. ####",
                },
                {
                    "role": "user",
                    "content": "How many degrees does the hour hand travel when the clock goes 246 minutes?",
                },
                {
                    "role": "assistant",
                    "content": "The hour hand travels 360 degrees in 12 hours, so every hour it travels 360/12=<T>divide(360,12)=30 degrees. 246 minutes is 246/60=<T>divide(246,60)=4.1 hours. The hour hand travels 4.1*30=<T>multiply(4.1,30)=123 degrees. ####",
                },
                {"role": "user", "content": question},
            ],
            tokenize=False,
            add_generation_prompt=True,
        )
    else:
        prompt = f"""
You are a helpful chatbot. You answer the following question using toolcalls to the tools: add, subtract, multiply, divide, power, sqrt, log, lcm, gcd, ln, choose, remainder, and permutate. You initiate the toolmode with the token <T>. You answer only the question the user provides you. End every answer with ####

Question: A coin is tossed 8 times, what is the probability of getting exactly 7 heads ?
Answer: The total number of possible outcomes to toss a coin 8 times is 2^8=<T>power(2,8)=256. The number of ways of getting exactly 7 heads is 8C7=<T>choose(8,7)=8. The probability of getting exactly 7 heads is 8/256=<T>divide(8,256)=0.03125. ####

Question: If paint costs $3.2 per quart, and a quart covers 12 square feet, how much will it cost to paint the outside of a cube 10 feet on each edge?
Answer: The total surface area of the 10 ft cube is 6*10^2=6*<T>power(10,2)=100=<T>multiply(6,100)=600 square feet. The number of quarts needed is 600/12=<T>divide(600,12)=50. The cost is 50*3.2=<T>multiply(50,3.2)=160. ####

Question: log(x)=2, log(y)=0.1, what is the value of log(x-y) ?
Answer: log(x)=2, so x=10^2=<T>power(10,2)=100; log(y)=0.1, so y=10^0.1=<T>power(10,0.1)=1.26; x-y=100-1.26=<T>subtract(10,1.26)=98.74, so log(x-y)=log(98.74)=<T>log(98.74)=1.99. ####

Question: How many degrees does the hour hand travel when the clock goes 246 minutes?
Answer: The hour hand travels 360 degrees in 12 hours, so every hour it travels 360/12=<T>divide(360,12)=30 degrees. 246 minutes is 246/60=<T>divide(246,60)=4.1 hours. The hour hand travels 4.1*30=<T>multiply(4.1,30)=123 degrees. ####

Question: {question}
Answer: 
"""
        prompt = prompt.strip() + " "
    return prompt


def main():
    # Load data
    data = load()["test"]

    # Load model
    device_map = f"cuda:{CUDA_DEVICE_ID}"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME, device_map=device_map, torch_dtype=torch.bfloat16, load_in_4bit=True
    )
    model.config.pad_token_id = model.config.eos_token_id
    tokenizer.pad_token = tokenizer.eos_token

    # Create decoder
    decoder = CfgDecoder(model, tokenizer)

    # Batch data
    batches = [data[i : i + BATCH_SIZE] for i in range(0, len(data), BATCH_SIZE)]

    # Generate
    is_correct_all = []
    for batch in tqdm(batches):
        questions = batch["question"]
        # prompts = [funcqa_prompt_multi_hop + "\n\nQuestion: " + q + "\nAnswer:" for q in questions]
        prompts = [create_prompt(q, tokenizer=tokenizer, use_chat_template=USE_CHAT_TEMPLATE) for q in questions]
        results = decoder.generate_interleaving(
            prompts,
            max_new_tokens_thinking=200,
            max_new_tokens_operation=50,
            use_constrained=True,
        )
        results_float = [float(r.result) if r.result is not None else float("nan") for r in results]
        is_correct = [
            math.isclose(res, answer, abs_tol=0.1, rel_tol=0.1)
            for res, answer in zip(results_float, batch["answer_number"])
        ]

        print(f"Question: {questions}")
        print(f"Answers: {[r.to_sentence() for r in results]}")
        print(f"Result Numbers: {results_float}")
        print(f"Correct Answer: {batch['answer_number']}")
        print(f"Is correct: {is_correct}")
        print("-" * 80)
        print()

        is_correct_all += is_correct
        print("Accuracy until now:", sum([1 for r in is_correct_all if r]) / len(is_correct_all))
        print(is_correct_all)

    print("Accuracy:", sum([1 for r in is_correct_all if r]) / len(is_correct_all))


if __name__ == "__main__":
    main()
