import os
from pathlib import Path

""" 
create a matrix of some sort -> go through every number and count the once adjecent to a symbol
"""

def is_symbol(char):
    return not char.isdigit() and char != '.'

def is_next_to_symbol(lines, i, j):
    left = max(0, j-1)
    right = min(len(lines[i]), j+2)
    for c in range(left, right):
        # check over and under
        if (i > 0 and is_symbol(lines[i-1][c])) or\
           (i+1 < len(lines) and is_symbol(lines[i+1][c])):
            return True
    # check sides
    if (j-1 >= 0 and is_symbol(lines[i][j-1])) or\
        (j+1 < len(lines[i]) and is_symbol(lines[i][j+1])):
        return True
    
# Tests
assert is_next_to_symbol([
    ['.', '.', '#', '.'],
    ['.', '5', '.', '.'],
    ['.', '.', '.', '.']
], 1, 1)
assert is_next_to_symbol([
    ['.', '5', '5', '.'],
    ['.', '.', '.', '#'],
    ['.', '.', '.', '.']
], 0, 2)

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')

sum1 = 0

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [list(line.strip()) for line in lines]

    for i in range(len(lines)):

        number = ""
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                number += lines[i][j]
                if is_next_to_symbol(lines, i, j):
                    # parse the number and add it to the sum
                    q = j + 1
                    while q < len(lines[i]) and lines[i][q].isdigit():
                        number += lines[i][q]
                        q += 1
                    lines[i][j:q] = ['.' for _ in range(q-j)]
                    sum1 += int(number)
            else:
                number = ""

print(sum1)
            

