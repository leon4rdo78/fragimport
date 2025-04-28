import random

# File names
input_file = 'gitMTNMCI'
output_file = 'selector/gitMTNMCIrandom'

# Number of lines to select
num_lines_to_select = 0

def select_random_lines(input_file, output_file, num_lines):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # If there are fewer lines than requested, use all lines
    if len(lines) <= num_lines:
        selected_lines = lines
    else:
        # Randomly sample lines without replacement
        selected_lines = random.sample(lines, num_lines)
    
    with open(output_file, 'w') as f:
        f.writelines(selected_lines)

if __name__ == "__main__":
    select_random_lines(input_file, output_file, num_lines_to_select)
