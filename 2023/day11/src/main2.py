import itertools
import os
from pathlib import Path


class Solution:
    def __init__(self, data: list[list[str] | str]):
        self.board = list(map(list, data))

    def solve(self, empty_multiplier: int) -> int:
        galaxies = set()
        empty_rows = set(range(len(self.board)))
        empty_columns = set(range(len(self.board[0])))

        for r, row in enumerate(self.board):
            for c, value in enumerate(row):
                if value == "#":
                    galaxies.add((r, c))
                    empty_columns -= {c}
                    empty_rows -= {r}

        s = 0

        for (r1, c1), (r2, c2) in itertools.combinations(galaxies, 2):
            if r1 > r2:
                r1, r2 = r2, r1
            if c1 > c2:
                c1, c2 = c2, c1

            for r in range(r1, r2):
                s += empty_multiplier if r in empty_rows else 1

            for c in range(c1, c2):
                s += empty_multiplier if c in empty_columns else 1

        return s

    def solve_part1(self):
        return self.solve(2)

    def solve_part2(self):
        return self.solve(1_000_000)


parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')
with open(abs_file_path) as file:
    board = Solution(file.read())
    print(f"Day 11. Part 1: {board.solve_part1()}")
    print(f"Day 11. Part 2: {board.solve_part2()}")
