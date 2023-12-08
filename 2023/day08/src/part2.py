import os
import math
from pathlib import Path

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')

# Using LCM (Least Common Multiple) to solve this problem by finding the number of steps
# for each starting node to reach the end node, then finding the LCM of all of those numbers

def next_node(node, instruction, nodes_dict):
    if instruction == 'L':
        return nodes_dict[node][0]
    else:
        return nodes_dict[node][1]

def solve(instructions, nodes_dict, starting_node):
    instruction_idx = 0
    current_node = starting_node
    steps = 0
    while current_node[2] != 'Z':
        instruction = instructions[instruction_idx]
        current_node = next_node(current_node, instruction, nodes_dict)
        instruction_idx = (instruction_idx + 1) % len(instructions)
        steps += 1
    return steps

with open(abs_file_path) as file:
    instructions, nodes = file.read().split('\n\n')
    nodes_dict = {}
    starting_nodes = set()
    for node in nodes.split('\n'):
        node = node.split(' = ')
        if node[0][2] == 'A':
            starting_nodes.add(node[0])
        nodes_dict[node[0]] = (node[1][1:4], node[1][6:9])

    ans2 = math.lcm(*set(solve(instructions, nodes_dict, starting_node) for starting_node in starting_nodes))
    print(f'Part 2: {ans2}')