# Stop on error
set -e

export CUDA_VISIBLE_DEVICES=1

# Untrained model, different configs
python3 -m toolmode.run --output_dir=eval/zephyr_untrained_16bit --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="16bit" 
python3 -m toolmode.run --output_dir=eval/zephyr_untrained_8bit --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="8bit" 
python3 -m toolmode.run --output_dir=eval/zephyr_untrained_4bit --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="4bit" 

# Untrained model without constrains
python3 -m toolmode.run --output_dir=eval/zephyr_untrained_16bit_unconstrained --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="16bit"  --do_not_use_constained

# Different trained models
python3 -m toolmode.run --output_dir=eval/zephyr_trained_4bit  --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="4bit" --adapter_name=models/zephyr_funcqa_4bit/final_checkpoint
python3 -m toolmode.run --output_dir=eval/zephyr_trained_16bit  --model_name="HuggingFaceH4/zephyr-7b-beta" --quantization="16bit" --adapter_name=models/zephyr_funcqa_16bit/final_checkpoint