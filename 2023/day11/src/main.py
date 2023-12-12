import copy
import os
import math
from pathlib import Path

class Universe:
    def __init__(self, grid):
        self.grid = grid

    def solve(self, expansion):
        galaxies = []
        empty_rows = set(range(len(self.grid)))
        empty_columns = set(range(len(self.grid[0])))

        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == "#":
                    galaxies.append((r, c))
                    empty_columns -= {c}
                    empty_rows -= {r}

        ans = 0
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                row_range = range(galaxies[i][0], galaxies[j][0]) if galaxies[i][0] < galaxies[j][0] else range(galaxies[j][0], galaxies[i][0])
                col_range = range(galaxies[i][1], galaxies[j][1]) if galaxies[i][1] < galaxies[j][1] else range(galaxies[j][1], galaxies[i][1])

                for r in row_range:
                    ans += expansion if r in empty_rows else 1
                for c in col_range:
                    ans += expansion if c in empty_columns else 1

        return ans
    
    def print_universe(self):
        for row in self.grid:
            print(''.join(row))

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')
with open(abs_file_path) as file:
    grid = [list(line.strip()) for line in file.readlines()]
    uni = Universe(grid)

    ans1 = uni.solve(2)
    ans2 = uni.solve(1000000)
    print(f'Part 1: {ans1}')
    print(f'Part 2: {ans2}')
