import os
import sys
from pathlib import Path

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')

sections = None
with open(abs_file_path) as file:
    sections = file.read().split('\n\n')

def solve(seed):
    current_seed = seed

    for i in range(1, 8):
        lines = sections[i].split('\n')[1:]
        for line in lines:
            dest, src, rng_len = [int(nbr) for nbr in line.split()]
            if src <= current_seed <= src + rng_len:
                current_seed = dest + current_seed - src
                break

    return current_seed

if __name__ == '__main__':

    with open(abs_file_path) as file:
        sections = file.read().split('\n\n')
        seeds = [int(nbr) for nbr in sections[0].split(':')[1].split()]

        # list of ranges for part 2
        seed_ranges = []
        for i in range(0, len(seeds), 2):
            seed_ranges.append(range(seeds[i], seeds[i] + seeds[i+1]))

        ans1 = min([solve(seed) for seed in seeds])
        print(f'Part 1: {ans1}')

        # very very very slow
        ans2 = sys.maxsize
        for r in seed_ranges:
            for seed in r:
                res = solve(seed)
                if res < ans2:
                    ans2 = res
        print(f'Part 2: {ans2}')