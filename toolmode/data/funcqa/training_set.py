import os
import json
import datasets as ds
import pandas as pd


FUNCQA_TRAINING_DATA = "data/funcqa/training_data"
FUNCQA_PROMPT_MULTI_HOP = "data/funcqa/template_mh/llama_general_tooldec.txt"
DATASETS_CACHE_DIR_PATH = "~/cache"


def get_funcqa_multi_hop_dataset():
    # Load files
    files = [os.path.join(FUNCQA_TRAINING_DATA, f) for f in os.listdir(FUNCQA_TRAINING_DATA)]
    rows = [open(f).readlines() for f in files]
    rows = [r for sublist in rows for r in sublist]
    rows = [json.loads(r) for r in rows]
    dataset = ds.Dataset.from_list(rows)

    # # Save and load the dataset to enable caching
    # cache_dir = os.path.join(DATASETS_CACHE_DIR_PATH, "funcqa_training_set")
    # dataset.save_to_disk(cache_dir)
    # dataset = ds.load_from_disk(cache_dir)

    return dataset


def change_operation_format(row):
    answer = row["answer"]
    # Replace < with [T] to avoid <T> being interpreted as a tag
    answer = answer.replace("<eoe>", "")
    answer = answer.replace("<", "[T]").replace(">", "").replace("[T]", "<T>")
    return {"answer": answer}


def add_prompt(row):
    with open(FUNCQA_PROMPT_MULTI_HOP, "r") as f:
        prompt = f.read()
    prompt = prompt.replace("[QUESTION]", row["question"])
    return {**row, "prompt": prompt}


def add_full_text(row):
    return {"text": row["prompt"] + row["answer"]}


def load():
    dataset = get_funcqa_multi_hop_dataset()
    dataset = dataset.map(change_operation_format, batched=False, load_from_cache_file=False)
    dataset = dataset.map(add_prompt, batched=False)
    dataset = dataset.map(add_full_text)
    return dataset
