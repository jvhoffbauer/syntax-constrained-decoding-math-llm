import torch
from transformers import AutoTokenizer

from toolmode.cfg_decoding.logits_processor import FsaGpu


def test_gpu_fsa():
    g = FsaGpu(AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta"))

    test_cases = [
        (
            "multip",
            {"ly"},
        ),
        (
            "multiply",
            {"("},
        ),
        (
            "add(",
            {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
        ),
        (
            "add(0",
            {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ")=", ","},
        ),
        ("permutate", {"("}),
        ("ln(1, 2)=", {"</s>"}),
        ("ln(1.", {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", ")="}),
    ]
    for input_str, expected_tokens in test_cases:
        input_tokens = torch.Tensor(g._encode(input_str)).long().unsqueeze(0)
        mask, _ = g.get_token_mask(input_tokens, torch.tensor([0]))
        tokens = g.tokenizer.convert_ids_to_tokens(torch.where(mask)[1].tolist())
        assert set(tokens) == expected_tokens, f"When running {input_str}, expected {expected_tokens}, got {tokens}"


def test_gpu_fsa_multibatch():
    g = FsaGpu(AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta"))

    test_cases = [
        (
            "multip",
            {"ly"},
        ),
        (
            "multiply",
            {"("},
        ),
        (
            "multiply(",
            {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
        ),
    ]

    input_tokens = g.tokenizer(["<T>" + s for s, _ in test_cases], padding=True, return_tensors="pt").input_ids
    start_indices = torch.where(input_tokens == g.tokenizer.vocab[">"])[1] + 1
    mask, _ = g.get_token_mask(input_tokens, start_indices=start_indices)

    for mask_row, (input_str, expected_tokens) in zip(mask, test_cases):
        tokens = g.tokenizer.convert_ids_to_tokens(torch.where(mask_row.unsqueeze(0))[1].tolist())
        assert set(tokens) == expected_tokens, f"When running {input_str}, expected {expected_tokens}, got {tokens}"
