import json
from collections import Counter

import toolmode.data.funcqa as funcqa


def main():
    dataset = funcqa.load()

    print(dataset)
    print(json.dumps(dataset[0], indent=2))


if __name__ == "__main__":
    main()
