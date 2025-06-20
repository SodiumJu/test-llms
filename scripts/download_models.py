from huggingface_hub import snapshot_download

base_dir = "LLM-models-download"

# Qwen
snapshot_download(
    repo_id="Qwen/Qwen2.5-Coder-7B",
    local_dir=f"{base_dir}/Qwen2.5-Coder-7B",
    local_dir_use_symlinks=False
)

# GPT2-XL
snapshot_download(
    repo_id="gpt2-xl",
    local_dir=f"{base_dir}/gpt2-xl",
    local_dir_use_symlinks=False
)

# LLaMA 3-7B（需先通過 Meta 許可並登入 Hugging Face）
snapshot_download(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    local_dir=f"{base_dir}/Meta-Llama-3-8B-Instruct",
    local_dir_use_symlinks=False
)

snapshot_download(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    local_dir=f"{base_dir}/Mistral-7B-Instruct-v0.2",
    local_dir_use_symlinks=False
)

snapshot_download(
    repo_id="google/gemma-2-9b",
    local_dir=f"{base_dir}/gemma-2-9b",
    local_dir_use_symlinks=False
)

snapshot_download(
    repo_id="deepseek-ai/DeepSeek-R1-0528-Qwen3-8B",
    local_dir=f"{base_dir}/DeepSeek-R1-0528-Qwen3-8B",
    local_dir_use_symlinks=False
)

snapshot_download(
    repo_id="deepseek-ai/deepseek-coder-7b-instruct-v1.5",
    local_dir=f"{base_dir}/deepseek-coder-7b-instruct-v1.5",
    local_dir_use_symlinks=False
)