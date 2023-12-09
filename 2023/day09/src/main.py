import os
from pathlib import Path

def create_sub_differences(line):
    sub_differences = [line]
    last_diff = line
    while any(nbr != 0 for nbr in last_diff):
        new_diff = []
        for i in range(len(last_diff) - 1):
            new_diff.append(last_diff[i+1] - last_diff[i])
        last_diff = new_diff
        sub_differences.append(last_diff)
    
    return sub_differences

def next_in_sequence(line):
    sub_differences = create_sub_differences(line)
    return sum([diff[-1] for diff in sub_differences])

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')

with open(abs_file_path) as file:
    lines = [[int(nbr) for nbr in line.strip().split()] for line in file.readlines()]
    
    ans1 = sum([next_in_sequence(line) for line in lines])
    print(f'Part 1: {ans1}')

    # reverse the sequence to get the first
    ans2 = sum([next_in_sequence(line[::-1]) for line in lines])
    print(f'Part 2: {ans2}')
