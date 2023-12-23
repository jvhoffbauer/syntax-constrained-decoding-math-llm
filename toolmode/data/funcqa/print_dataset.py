import json
from collections import Counter

from toolmode.data.funcqa import training_set
from transformers import AutoTokenizer


def main():
    dataset = training_set.load()

    print(dataset)
    print(json.dumps(dataset[0], indent=2))

    # Get longest sequence
    tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-alpha")
    print("Max tokens:", max(dataset.map(lambda x: {"length": len(tokenizer.encode(x["text"]))})["length"]), "tokens")


if __name__ == "__main__":
    main()
