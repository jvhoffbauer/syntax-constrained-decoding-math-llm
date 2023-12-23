from datasets import load_dataset
from trl import SFTTrainer
from transformers import AutoModelForCausalLM, AutoTokenizer, LogitsProcessorList
from peft import LoraConfig
from toolmode.data.funcqa import training_set
from peft import get_peft_config, get_peft_model, LoraConfig, TaskType
from transformers.training_args import TrainingArguments
import argparse
import os
from dataclasses import dataclass, field
from os.path import join
from typing import Optional

import peft
import torch
from peft import (
    LoraConfig,
    PeftConfig,
    PeftModel,
    TaskType,
    get_peft_model,
    set_peft_model_state_dict,
)
from peft.utils import _get_submodules
from transformers import (
    AutoConfig,
    AutoModelForCausalLM,
    AutoModelForSequenceClassification,
    AutoTokenizer,
    HfArgumentParser,
)

MODEL_NAME = "HuggingFaceH4/zephyr-7b-alpha"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run_name", type=str)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--max_seq_length", type=int, default=1024)
    args = parser.parse_args()

    dataset = training_set.load()

    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        load_in_4bit=True,
        device_map="cuda:0",
    )
    model = get_peft_model(model, lora_config)

    train_args = TrainingArguments(
        output_dir=os.path.join(args.run_name, "output"),
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        gradient_accumulation_steps=32,
        num_train_epochs=args.epochs,
    )
    trainer = SFTTrainer(
        model,
        args=train_args,
        train_dataset=dataset,
        dataset_text_field="text",
        max_seq_length=256,
    )
    trainer.train()
    trainer.save_model(os.path.join(args.run_name, "checkpoints"))

    # Merge and save the model
    model_merged = PeftModel.from_pretrained(
        AutoModelForCausalLM.from_pretrained(MODEL_NAME, return_dict=True, torch_dtype=torch.bfloat16),
        os.path.join(args.run_name, "checkpoints"),
    )
    model_merged = model_merged.merge_and_unload()
    model_merged.save_pretrained(os.path.join(args.run_name, "merged_model_final"))
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenizer.save_pretrained(os.path.join(args.run_name, "merged_model_final"))


if __name__ == "__main__":
    main()
