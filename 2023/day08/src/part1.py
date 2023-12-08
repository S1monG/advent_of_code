import os
from pathlib import Path

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')

def solve(instructions, nodes_dict):
    instruction_idx = 0
    current_node = 'AAA'
    steps = 0
    while current_node != 'ZZZ':
        instruction = instructions[instruction_idx]
        if instruction == 'L':
            current_node = nodes_dict[current_node][0]
        else:
            current_node = nodes_dict[current_node][1]
        instruction_idx = (instruction_idx + 1) % len(instructions)
        steps += 1
    return steps



with open(abs_file_path) as file:
    instructions, nodes = file.read().split('\n\n')
    nodes_dict = {}
    for node in nodes.split('\n'):
        node = node.split(' = ')
        nodes_dict[node[0]] = (node[1][1:4], node[1][6:9])

    ans1 = solve(instructions, nodes_dict)
    print(f'Part 1: {ans1}')
