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

def history_forwards(line):
    sub_differences = create_sub_differences(line)
    return sum([diff[-1] for diff in sub_differences])

def history_backwards(line):
    sub_differences = create_sub_differences(line)
    history_sum = 0
    sign = 1
    for diff in sub_differences:
        history_sum += diff[0] * sign
        sign = sign * -1
    return history_sum

assert history_backwards([10, 13, 16, 21, 30, 45]) == 5
assert history_backwards([1, 3, 6, 10, 15, 21]) == 0


parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')

with open(abs_file_path) as file:
    lines = [[int(nbr) for nbr in line.strip().split()] for line in file.readlines()]
    
    ans1 = sum([history_forwards(line) for line in lines])
    print(f'Part 1: {ans1}')

    ans2 = sum([history_backwards(line) for line in lines])
    print(f'Part 1: {ans2}')
