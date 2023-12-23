import json
from collections import Counter

from transformers import AutoTokenizer

from toolmode.data.funcqa import load


def main():
    dataset = load()
    print(dataset)

    print("\nTrain:")
    print(json.dumps(dataset["train"][0], indent=2))
    print("\nTest:")
    print(json.dumps(dataset["test"][0], indent=2))
    # # Get longest sequence
    # tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-alpha")
    # print("Max tokens:", max(dataset.map(lambda x: {"length": len(tokenizer.encode(x["text"]))})["length"]), "tokens")


if __name__ == "__main__":
    main()
