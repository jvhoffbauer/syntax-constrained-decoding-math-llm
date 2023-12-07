import os

import datasets as ds
import pandas as pd

FUNCQA_DATASET_FILE_PATH = "data/funcqa/funcqa_oh.json"
FUNCQA_PROMPT_TEMPLATE_FILE_FMT = "data/funcqa/template_oh/llama_<{operation}>.txt"
DATASETS_CACHE_DIR_PATH = "/scratch1/redditqa/cached_datasets"


def get_funcqa_dataset():
    # Load the dataset
    dataset = ds.Dataset.from_pandas(pd.read_json(FUNCQA_DATASET_FILE_PATH, orient="records"))

    # Save and load the dataset to enable caching
    cache_dir = os.path.join(DATASETS_CACHE_DIR_PATH, os.path.basename(FUNCQA_DATASET_FILE_PATH))
    dataset.save_to_disk(cache_dir)
    dataset = ds.load_from_disk(cache_dir)

    return dataset


def create_prompt(row):
    # Get first text in angle brackets, i.e. <TEXT>
    operation = row["func"].split("<")[1].split(">")[0]
    row["operation"] = operation

    # Get the prompt
    prompt_template_file_path = FUNCQA_PROMPT_TEMPLATE_FILE_FMT.format(operation=operation)
    with open(prompt_template_file_path, "r") as f:
        prompt_template = f.read()
    prompt = prompt_template.replace("[QUESTION]", row["question"])
    row["prompt"] = prompt

    return row


def change_operation_format(row):
    cols_to_change = ["func", "prompt"]
    for col in cols_to_change:
        row[col] = row[col].replace("<", "[T]").replace(">", "").replace("[T]", "<T>")
        # Avoid replacing instructions
        row[col] = row[col].replace(f"the operator <T>{row['operation']}", f"the operator {row['operation']}")
    return row


def load():
    dataset = get_funcqa_dataset()
    dataset = dataset.map(create_prompt, batched=False)
    # Disable caching for this step
    dataset = dataset.map(change_operation_format, batched=False)
    return dataset
