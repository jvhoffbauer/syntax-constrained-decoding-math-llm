import json
import os
import re

import datasets as ds
import pandas as pd

FUNCQA_MULTI_HOP_DATASET_FILE_PATH = "data/funcqa/funcqa_mh.json"
FUNCQA_PROMPT_MULTI_HOP = "data/funcqa/template_mh/llama_general_tooldec.txt"
DATASETS_CACHE_DIR_PATH = "/scratch1/redditqa/cached_datasets"
FUNCQA_TRAINING_DATA = "data/funcqa/training_data"
FUNCQA_PROMPT_MULTI_HOP = "data/funcqa/template_mh/llama_general_tooldec.txt"
DATASETS_CACHE_DIR_PATH = "~/cache"


# Load the multi hop prompt
with open(FUNCQA_PROMPT_MULTI_HOP, "r") as f:
    funcqa_prompt_multi_hop = f.read()


def change_operation_format_in_answer(row: dict) -> dict:
    answer = _change_operation_format(row["answer"])
    return {"answer": answer}


def _change_operation_format(s: str) -> str:
    # Replace < with [T] to avoid <T> being interpreted as a tag
    # s = s.replace("<eoe>", "")
    s = re.sub(r"<eoe>\d+(\.\d+)?", "", s)
    s = s.replace("<", "[T]").replace(">", "").replace("[T]", "<T>")
    return s


def get_answer_numerical(row: dict) -> dict:
    answer = row["answer"]

    # The result is the number after the last <eoe> tag
    answer = answer.split("<eoe>")[-1].split(" ")[0]

    # Remove trailing punctuation
    if answer[-1] == "." or answer[-1] == "," or answer[-1] == "%":
        answer = answer[:-1]

    # Parse as float
    answer = float(answer)

    return {"answer_number": answer}


def add_prompt(row):
    prompt = funcqa_prompt_multi_hop.replace("[QUESTION]", row["question"])
    return {"prompt": prompt}


def load():
    # Load test data
    test = ds.Dataset.from_pandas(pd.read_json(FUNCQA_MULTI_HOP_DATASET_FILE_PATH, orient="records"))
    test = test.remove_columns(["calculation"])

    # Load train files
    files = [os.path.join(FUNCQA_TRAINING_DATA, f) for f in os.listdir(FUNCQA_TRAINING_DATA)]
    rows = [open(f).readlines() for f in files]
    rows = [r for sublist in rows for r in sublist]
    rows = [json.loads(r) for r in rows]
    train = ds.Dataset.from_list(rows)

    # Preprocess test data
    test = test.rename_column("answer", "answer_number")
    test = test.map(lambda _: {"answer": ""}, batched=False)

    # Preprocess train data
    train = train.map(get_answer_numerical, batched=False)
    train = train.map(change_operation_format_in_answer, batched=False)

    # Create dataset dict
    dataset = ds.DatasetDict({"train": train, "test": test})
    dataset = dataset.map(add_prompt, batched=False)

    # Push to hub
    dataset.push_to_hub("jvhoffbauer/funcqa", private=True)

    return dataset
