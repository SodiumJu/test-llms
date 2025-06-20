from transformers import AutoModelForCausalLM, AutoTokenizer

import sys
import torch
import json
import time
import statistics
import os

def inference(file, out_dir, load_model_path=""):
    test_sample_num = 50
    if load_model_path == "":
        load_model_path = "Qwen/Qwen2.5-Coder-7B"
    lines = None
    prompt = ""
    prefix = "Please write a Python function to solve this problem.\n\n"
    with open(file, 'r', encoding='utf-8') as jsonl_file:
        lines = jsonl_file.readlines()  # Read all lines from the file

    # model = AutoModelForCausalLM.from_pretrained(
    #     load_model_path,
    #     trust_remote_code=True,
    #     # torch_dtype=torch.bfloat16,
    #     # torch_dtype=torch.float32,
    #     # device_map="balanced_low_0",
    #     device_map="auto",
    #     # attn_implementation="flash_attention_2", # add this can solve
    # ).to("cuda")
    model = AutoModelForCausalLM.from_pretrained(
        load_model_path,
        trust_remote_code=True,
        device_map="auto",
    )
    tokenizer = AutoTokenizer.from_pretrained(load_model_path, trust_remote_code=True)

    max_new_tokens = 300
    inference_time_list = []
    for j in range(len(lines)):
        if j >= test_sample_num:
            break
        question_data = json.loads(lines[j].strip())
        question_id = question_data['questionId']
        prompt = question_data['content']
        if prompt == None or prompt == "":
            print(f"Line {j} does not exist in the file. The file has {len(lines)} lines.")
            continue
        else:
            task_prompt = prompt + "\n\n" + prefix
            time_start = time.time()
            inputs = tokenizer(task_prompt, return_tensors="pt").to(model.device)

            # inputs = tokenizer(task_prompt, return_tensors="pt", padding=True).to(model.device)
            outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
            pred = tokenizer.decode(outputs[0], skip_special_tokens=True)
            time_end = time.time()
            inference_time = time_end - time_start
            inference_time_list.append(inference_time)

            print(f"Question ID: {question_id}, Inference Time: {inference_time} seconds")
            with open(f"{out_dir}/time.log", "a", encoding="utf-8") as f:
                f.write(f"Question ID: {question_id}, Inference Time: {inference_time} seconds\n")
            with open(f"{out_dir}/{question_id}.txt", "w", encoding="utf-8") as f:
                f.write(pred)
    avg = sum(inference_time_list) / len(inference_time_list)
    std = statistics.stdev(inference_time_list) if len(inference_time_list) > 1 else 0.0
    print(f"Average inference time: {avg:.4f} seconds, std: {std:.4f}")
    with open(f"{out_dir}/time.log", "a", encoding="utf-8") as f:
        f.write(f"Average inference time: {avg:.4f} seconds, std: {std:.4f}\n")
    

if __name__ == "__main__":
    # args 
    file = sys.argv[1]
    out_dir = sys.argv[2]

    # if out_dir does not exist, create it recursively
    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    load_model_path = sys.argv[3] if len(sys.argv) > 3 else ""
    inference(file, out_dir, load_model_path)
