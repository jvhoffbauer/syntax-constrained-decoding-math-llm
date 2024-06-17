export CUDA_VISIBLE_DEVICES=0
python3 -m toolmode.train --output_dir="models/zephyr_funcqa_16bit" --epochs=5 --quantization="16bit" --device="cuda:0"

export CUDA_VISIBLE_DEVICES=1
python3 -m toolmode.train --output_dir="models/zephyr_funcqa_8bit" --epochs=5 --quantization="8bit" --device="cuda:0"

export CUDA_VISIBLE_DEVICES=2
python3 -m toolmode.train --output_dir="models/zephyr_funcqa_4bit" --epochs=5 --quantization="4bit" --device="cuda:0"

export CUDA_VISIBLE_DEVICES=3
python3 -m toolmode.train --output_dir="models/zephyr_funcqa_16bit_endtoken" --epochs=5 --quantization="16bit"

export CUDA_VISIBLE_DEVICES=4
python3 -m toolmode.train --output_dir="models/zephyr_funcqa_16bit_endtoken_gsm8k" --epochs=3 --quantization="16bit" --add_gsm8k