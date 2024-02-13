# Stop on error
set -e

export CUDA_VISIBLE_DEVICES=0

# # Untrained model, different configs
# python3 -m toolmode.run --output_dir=eval/zephyr_untrained_16bit --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="16bit" 
# python3 -m toolmode.run --output_dir=eval/zephyr_untrained_8bit --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="8bit" 
# python3 -m toolmode.run --output_dir=eval/zephyr_untrained_4bit --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="4bit" 

# # Untrained model without constrains
# python3 -m toolmode.run --output_dir=eval/zephyr_untrained_16bit_unconstrained --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="16bit"  --do_not_use_constained

# # Different trained models
# python3 -m toolmode.run --output_dir=eval/zephyr_trained_4bit  --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="4bit" --adapter_name=models/zephyr_funcqa_4bit/final_checkpoint
# python3 -m toolmode.run --output_dir=eval/zephyr_trained_16bit  --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="16bit" --adapter_name=models/zephyr_funcqa_16bit/final_checkpoint

# # Model with GSM8k
# python3 -m toolmode.run --output_dir=eval/zephyr_trained_16bit_gsm8k  --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="16bit" --adapter_name=models/zephyr_funcqa_16bit_gsm8k/output/checkpoint-470

# python3 -m toolmode.run --output_dir=eval/zephyr_funcqa_16bit_endtoken  --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="16bit" --adapter_name=models/zephyr_funcqa_16bit_endtoken/output/checkpoint-80
# python3 -m toolmode.run --output_dir=eval/zephyr_funcqa_16bit_endtoken_gsm8k  --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="16bit" --adapter_name=models/zephyr_funcqa_16bit_endtoken_gsm8k/output/checkpoint-430

# Eval models on GSM8k
python3 -m toolmode.run --output_dir=eval/gsm8k_test/zephyr_trained_16bit_gsm8k --dataset=gsm8k --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="16bit" --adapter_name=models/zephyr_funcqa_16bit_gsm8k/output/checkpoint-470
python3 -m toolmode.run --output_dir=eval/gsm8k_test/zephyr_trained_16bit --dataset=gsm8k --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="16bit" --adapter_name=models/zephyr_funcqa_16bit/final_checkpoint
