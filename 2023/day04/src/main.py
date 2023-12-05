import os
from pathlib import Path

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')

def get_score1(winning_numbers, my_numbers):
    score = 0
    for nbr in winning_numbers:
        if nbr in my_numbers:
            score += 1
    return 2 ** (score - 1) if score > 0 else 0

assert get_score1([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 16

sum1 = 0
with open(abs_file_path) as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
        splitted = line.split(':')[1].split('|')
        winning_numbers = [int(nbr) for nbr in splitted[0].split()]
        my_numbers = [int(nbr) for nbr in splitted[1].split()]

        sum1 += get_score1(winning_numbers, my_numbers)
print(f'Part 1: {sum1}')

# Part 2

def get_score2(winning_numbers, my_numbers):
    score = 0
    for nbr in winning_numbers:
        if nbr in my_numbers:
            score += 1
    return score

assert get_score2([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 5

def solve(lines):
    nbr_of_copies = dict()
    for i in range(len(lines)): # initialize all copies to 1
        nbr_of_copies[i] = 1

    for i in range(len(lines)):
        card = lines[i]
        score = get_score2(card[0], card[1])
        copies = nbr_of_copies.get(i)
        for idx in range(score):
            nbr_of_copies[idx+i+1] = nbr_of_copies.get(idx+i+1) + copies

    return sum(nbr_of_copies.values())
        

with open(abs_file_path) as file:
    lines = [line.strip() for line in file.readlines()]
    lines = [line.split(':')[1].split('|') for line in lines]
    lines = [[[int(nbr) for nbr in line[0].split()], [int(nbr) for nbr in line[1].split()]] for line in lines]
    print(f'Part 2: {solve(lines)}')
    



        