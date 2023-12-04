import os
from pathlib import Path

colors = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def solve(input):
    a = input.split(':')[1].split(';') # removes game index
    for nbr_string_pairs in a:
        l = nbr_string_pairs.split(',')
        for pair in l:
            nbr = int(pair.split()[0])
            color = pair.split()[1].strip()
            if colors[color] < nbr:
                return False
    return True
            
def solve2(input):
    a = input.split(':')[1].split(';') # removes game index
    d = {"red": 0, "green": 0, "blue": 0}
    for nbr_string_pairs in a:
        l = nbr_string_pairs.split(',')

        for pair in l:
            nbr = int(pair.split()[0])
            color = pair.split()[1].strip()
            if d[color] < nbr:
                d[color] = nbr
    res = 1
    for v in d.values():
        res*=v
    return res

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')

sum1 = 0
sum2 = 0
with open(abs_file_path) as file:
    for idx, line in enumerate(file):
        if solve(line):
            sum1 += idx + 1
        sum2 += solve2(line)
print(sum1)
print(sum2)

