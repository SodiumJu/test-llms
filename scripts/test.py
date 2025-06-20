import sys
import os
import re
sys.path.append('/workspace')
from env.Sokoban import SokobanGenerator
# from LLM_generater.llama2_13b import tokenizer, model, device, generate_text
# from LLM_generater.llama3_70b import tokenizer, model, device, generate_text
# from LLM_generater.llama2_13b_gym_trajectory_data import tokenizer, model, device, generate_text
import tools.png_to_gif
from LLM_generater.llama2_13b_sp_bfs_trajectory import tokenizer, model, device, generate_text
sokoban = SokobanGenerator()
example_folder_path = "datasets/bfs-sp-dataset/train/game-2"
output_folder_path = "experiments/simple-bfs-examples-output"
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

def combine_prompt(prompt):
    prompt_text = ""
    i = 0
    for prompt_unit in prompt:
        if i == 0:
            prompt_text += f"state:\n{prompt_unit['state']}\n"
        else:
            prompt_text += f"action:{prompt_unit['action']}\n"
            prompt_text += f"state:\n{prompt_unit['state']}\n"
        i += 1
    return prompt_text

# load sokoban example
# with open(f"{example_folder_path}/sokoban_map-train-2.txt", "r") as f:
#     solve_example = f.read()
solve_example = ""
goal_text = "Goal: given a Sokoban state, assign an action for the agent (@), and make the box ($) close to the goal (X).\n"
goal_text += "Just use @ to push $, make $ to X.\n"

file_id = 0
game_count = 0
win_count = 0
for file_id in range(3, 51):
    game_count += 1
    # example_folder_path = f"datasets/bfs-sp-dataset/train/game-{file_id}"
    # example_folder_path = f"datasets/bfs-sp-dataset/test/sokoban_map-test-{file_id}.txt"
    # for file_name in os.listdir(example_folder_path):
    # if file_name.endswith('.txt'):
        # sokoban_file_name = f"{example_folder_path}/{file_name}"
    # sokoban_file_name = f"datasets/bfs-sp-dataset/test/sokoban_map-test-{file_id}.txt"
    sokoban_file_name = f"datasets/bfs-sp-dataset/train/game-{file_id}/sokoban_map-train-{file_id}.txt"
    sokoban.reset()
    sokoban.load_from_txt(sokoban_file_name)
    max_length = 150
    prompt = []
    
    # with open(sokoban_file_name, "r") as f:

    action = "none"
    for l in range(25):
        prompt_unit = {
            "state": sokoban.display(),
            "action": action
        }
        prompt.append(prompt_unit)
        if len(prompt) > 3:
            prompt.pop(0)
        input_text = combine_prompt(prompt)
        # input_text = goal_text + solve_example + "\n\nNow you solve:\n" + input_text
        input_text += "action:"
        print()
        print("Prompt:")
        print(input_text)
        generated_text = generate_text(input_text, max_length=max_length + 140, temperature=0.5, top_k=50, top_p=0.95)
        # print("Generated text:")
        # print(generated_text)
        cleaned_text = generated_text.replace(input_text[:-8], "", 1)
        
        # actions = re.findall(r"action:(.*)", cleaned_text)
        # print(actions)
        # for action in actions:
        #     if action in sokoban.get_actions():
        #         sokoban.act(action)
        #         sokoban.render_to_image(f"{output_folder_path}/{l}.png")
        #         if sokoban.is_game_over:
        #             print("Game over!")
        #             break
        # print("Cleaned text:")
        # print(cleaned_text)
        # action = re.search(r"action:(.*)\n", cleaned_text)
        actions = re.findall(r"action:(.*)", cleaned_text)
        action = actions[0]
        if action:
            # action = action.group(1).strip()
            if action in sokoban.get_actions():
                sokoban.act(action)
                # print(f"action: {action}")
                # print(sokoban.display())
                sokoban.render_to_image(f"{output_folder_path}/{l}.png")
                if sokoban.is_game_over:
                    print("Game over!")
                    break
        else:
            print("No action found!")
    if sokoban.win == True:
        print("Win!")
        win_count += 1
    tools.png_to_gif.create_gif_from_pngs(output_folder_path, f"{output_folder_path}/train-{file_id}.gif")
    print(f"win: {win_count}/{game_count}")
    print(f"win rate: {win_count/game_count}")