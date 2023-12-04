import os

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
            


script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

sum1 = 0
with open(abs_file_path) as file:
    for idx, line in enumerate(file):
        if solve(line):
            sum1 += idx + 1
print(sum1)

