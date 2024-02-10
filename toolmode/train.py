import argparse
import os

import datasets as ds
import torch
from peft import LoraConfig, PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, logging, set_seed
from transformers.training_args import TrainingArguments
from trl import SFTTrainer

import wandb
from toolmode.data.funcqa import load as load_funcqa
from toolmode.prompt import create_prompt

MODEL_NAME = "HuggingFaceH4/zephyr-7b-beta"
SEED = 42
set_seed(SEED)


logging.set_verbosity_info()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", type=str)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--max_seq_length", type=int, default=860)
    parser.add_argument("--quantization", type=str, default="none")
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--add_gsm8k", action="store_true", default=False)
    args = parser.parse_args()

    # Init wandb logging
    run_name = os.path.basename(args.output_dir)
    wandb.init(entity="funcqa-hpi", project="toolmode", name=run_name)

    # Load dataset
    dataset = load_funcqa()
    if args.add_gsm8k:
        dataset_gsm8k = ds.load_dataset("jvhoffbauer/gsm8k-toolcalls")
        print(f"Loaded gsm8k dataset: {dataset_gsm8k}")
        dataset_new = ds.DatasetDict(
            {split: ds.concatenate_datasets([dataset[split], dataset_gsm8k[split]]) for split in dataset.keys()}
        )
        dataset_new = dataset_new.shuffle(42)
        dataset = dataset_new

    dataset = dataset.map(
        lambda row: {"text": create_prompt(row["question"], use_chat_template=False) + row["answer"] + " ####"}
    )
    print(f"Has dataset: {dataset}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    sequence_lengths_tokens = [len(tokenizer.encode(row["text"])) for row in dataset["train"]]
    longest_sequence_tokens = max(sequence_lengths_tokens)
    mean_sequence_tokens = sum(sequence_lengths_tokens) / len(sequence_lengths_tokens)
    print(f"Longest train sequence tokens: max={longest_sequence_tokens} mean={mean_sequence_tokens}")

    # Define the lora config
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        target_modules=["q_proj", "k_proj"],
        task_type="CAUSAL_LM",
    )

    # Load the model
    # print(f"Quantization kwargs: {quantization_kwargs}")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        device_map=args.device,
        **get_quantization_kwargs(args.quantization),
    )

    # Train the model
    train_args = TrainingArguments(
        output_dir=os.path.join(args.output_dir, "output"),
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
        train_dataset=dataset["train"],
        eval_dataset=dataset["eval"],
        dataset_text_field="text",
        max_seq_length=args.max_seq_length,
        peft_config=lora_config,
    )
    trainer.train()
    trainer.save_model(os.path.join(args.output_dir, "final_checkpoint"))

    # # Merge and save the model
    # model_merged = PeftModel.from_pretrained(
    #     AutoModelForCausalLM.from_pretrained(
    #         MODEL_NAME,
    #         device_map=args.device,
    #         **quantization_kwargs,
    #     ),
    #     os.path.join(args.output_dir, "final_checkpoint"),
    # )
    # model_merged = model_merged.merge_and_unload()
    # model_merged.save_pretrained(os.path.join(args.output_dir, "final_checkpoint_merged"))
    # tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    # tokenizer.save_pretrained(os.path.join(args.output_dir, "final_checkpoint_merged"))


def get_quantization_kwargs(quantization: str):
    if quantization == "4bit":
        return {"load_in_4bit": True}
    elif quantization == "8bit":
        return {"load_in_8bit": True}
    elif quantization == "16bit":
        return {"torch_dtype": torch.bfloat16}
    elif quantization == "none":
        return {}
    else:
        raise ValueError(f"Unknown quantization: {quantization}")


if __name__ == "__main__":
    main()
