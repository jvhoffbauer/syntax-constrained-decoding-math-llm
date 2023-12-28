import argparse
import os

import torch
from peft import LoraConfig, PeftModel, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer, logging
from transformers.training_args import TrainingArguments
from trl import SFTTrainer

import wandb
from toolmode.data.funcqa import load as load_funcqa
from toolmode.run import create_prompt

MODEL_NAME = "HuggingFaceH4/zephyr-7b-beta"
SEED = 42


logging.set_verbosity_info()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run_name", type=str)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--max_seq_length", type=int, default=860)
    args = parser.parse_args()

    wandb.init(project="funcqa", name=args.run_name)

    dataset = load_funcqa()
    dataset = dataset.map(lambda row: {"text": create_prompt(row["question"], use_chat_template=False) + row["answer"]})
    train_and_eval_data = dataset["train"].shuffle(SEED).train_test_split(test_size=0.1)
    train_data, eval_data = train_and_eval_data["train"], train_and_eval_data["test"]

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

    train_args = TrainingArguments(
        output_dir=os.path.join(args.run_name, "output"),
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        gradient_accumulation_steps=32,
        num_train_epochs=args.epochs,
        evaluation_strategy="steps",
        save_strategy="steps",
        logging_steps=1,
        eval_steps=10,
        save_steps=10,
        report_to="wandb",
    )
    trainer = SFTTrainer(
        model,
        args=train_args,
        train_dataset=train_data,
        eval_dataset=eval_data,
        dataset_text_field="text",
        max_seq_length=args.max_seq_length,
        peft_config=lora_config,
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
