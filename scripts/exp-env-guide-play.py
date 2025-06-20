import sys
import os
sys.path.append('/workspace')

from env.Sokoban import SokobanGenerator

sokoban = SokobanGenerator()

example_folder_path = "experiments/simple-examples"

def EvalSample(sample):
    pass

for file_name in os.listdir(example_folder_path):
    if file_name.endswith('.txt'):
        with open(f"{example_folder_path}/{file_name}", "r") as f:
            sample = f.read()
            EvalSample(sample)
            

