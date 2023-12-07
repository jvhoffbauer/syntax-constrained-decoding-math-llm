import os

import datasets as ds
import pandas as pd

FUNCQA_MULTI_HOP_DATASET_FILE_PATH = "data/funcqa/funcqa_mh.json"
FUNCQA_PROMPT_MULTI_HOP = "data/funcqa/template_mh/llama_general_tooldec.txt"
DATASETS_CACHE_DIR_PATH = "/scratch1/redditqa/cached_datasets"


def get_funcqa_multi_hop_dataset():
    # Load the dataset 
    dataset = ds.Dataset.from_pandas(pd.read_json(FUNCQA_MULTI_HOP_DATASET_FILE_PATH, orient="records"))

    # # Save and load the dataset to enable caching
    # cache_dir = os.path.join(DATASETS_CACHE_DIR_PATH, os.path.basename(FUNCQA_MULTI_HOP_DATASET_FILE_PATH))
    # dataset.save_to_disk(cache_dir)
    # dataset = ds.load_from_disk(cache_dir)

    return dataset


def change_operation_format(row):
    calculations = []
    for calculation in row["calculation"]: 
        # Replace < with [T] to avoid <T> being interpreted as a tag
        calculation = calculation.replace("<", "[T]").replace(">", "").replace("[T]", "<T>")
        calculations.append(calculation)
    return row


def load():
    dataset = get_funcqa_multi_hop_dataset()
    dataset = dataset.map(change_operation_format, batched=False)
    return dataset
