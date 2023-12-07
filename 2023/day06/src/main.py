import os
from pathlib import Path

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')

""" 

y = traveled distance
x = waiting time

C = time for race
M = distance to beat

y = x * (C-x)

count all x where y > M

"""

def solve(time_dist_map):
    ans = 1
    for time, dist in time_dist_map.items():
        nbr_of_ways = 0
        for i in range(time):
            distance_traveled = i * (time - i)
            if distance_traveled > dist:
                nbr_of_ways += 1
        ans *= nbr_of_ways

    return ans


with open(abs_file_path) as file:
    lines = file.read().split('\n')
    time_dist_map = {}
    timelist, distlist = [line.split(':')[1].split() for line in lines]
    for i in range(len(timelist)):
        time_dist_map[int(timelist[i])] = int(distlist[i])

    ans1 = solve(time_dist_map)
    print(ans1)

with open(abs_file_path) as file:
    lines = file.read().split('\n')
    lines = [int(line.split(':')[1].replace(' ', '')) for line in lines]
    time_dist_map = {lines[0]: lines[1]}
    ans2 = solve(time_dist_map)
    print(ans2)