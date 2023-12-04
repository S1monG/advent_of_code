import os
from pathlib import Path

number_string_representation = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def starts_with(string):
    for key in number_string_representation:
        if string.startswith(key):
            return number_string_representation[key]
        
# bad name for this function
def ends_with(string):
    for key in number_string_representation:
        if string.startswith(key[::-1]):
            return number_string_representation[key]

def solve(input):
    res = 0
    for char in input:
        if char.isdigit():
            res += int(char) * 10
            break

    for char in input[::-1]:  # This is how you reverse a string in Python
        if char.isdigit():
            res += int(char)
            return res
        
def solve2(input):
    res = 0
    for i in range(len(input)):
        if input[i].isdigit():
            res += int(input[i]) * 10
            break
        a = starts_with(input[i:])
        if a:
            res += a * 10
            break
    
    reversed = input[::-1]
    for i in range(len(reversed)):
        if reversed[i].isdigit():
            res += int(reversed[i])
            return res
        a = ends_with(reversed[i:])
        if a:
            res += a
            return res
    

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')

sum1 = 0
sum2 = 0
with open(abs_file_path) as file:
    for line in file:
        sum1 += solve(line)
        sum2 += solve2(line)
print(sum1)
print(sum2)
