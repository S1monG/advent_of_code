import os
from pathlib import Path

def combinations(springs):
    spring_combinations = set()
    spring_combinations.add(springs)
    for i in range(len(springs)):
        if springs[i] == '?':
            to_be_removed = set()
            to_be_added = set()
            for spring in spring_combinations:
                to_be_added.add(spring[:i] + '#' + spring[i+1:])
                to_be_added.add(spring[:i] + '.' + spring[i+1:])
                to_be_removed.add(spring)
            spring_combinations -= to_be_removed
            spring_combinations |= to_be_added

            
    return spring_combinations

def valid_combination(springs, arrengement):
    return arrengement == list(filter(lambda count: count != 0 ,map(lambda x: x.replace('.', '').count('#'), springs.split('.'))))

assert valid_combination('##..#.#..##', [2, 1, 1, 2])
assert not valid_combination('#..##.#..##', [2, 1, 1, 2])

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')
with open(abs_file_path) as file:
    rows = []
    for line in file:
        line = line.strip().split()
        rows.append((line[0], list(map(int, line[1].split(',')))))
    # in the format [ ('????#?##.????#', [4, 2, 1, 2]), ('???????##?#?????.?', [4, 8, 1, 1]) ]

    ans = 0
    for springs, arrangement in rows:
        for comb in combinations(springs):
            if valid_combination(comb, arrangement):
                ans += 1
    
    print(f'Part 1: {ans}')



