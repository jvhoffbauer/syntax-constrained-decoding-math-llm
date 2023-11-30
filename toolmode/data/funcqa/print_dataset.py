import json
from collections import Counter

import toolmode.data.funcqa as funcqa


def main():
    dataset = funcqa.load()

    print(dataset)
    print(json.dumps(dataset[0], indent=2))
    print(Counter([row["operation"] for row in dataset]))
    print(dataset[0]["prompt"])


if __name__ == "__main__":
    main()
