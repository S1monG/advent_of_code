import os
import math
from pathlib import Path
from enum import Enum
 
class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

class PipeMap:
    def __init__(self, string_rep, width):
        self.width = width
        self.pipe_map = string_rep

    def get_elem_in_dir(self, pos, dir: Direction):
        match dir:
            case Direction.LEFT:
                return self.pipe_map[pos - 1]
            case Direction.RIGHT:
                return self.pipe_map[pos + 1]
            case Direction.UP:
                return self.pipe_map[pos - self.width]
            case Direction.DOWN:
                return self.pipe_map[pos + self.width]

    # change element to step count and
    # returns the next position with the direction it comes from
    def next_step_rec(self, pos, from_dir: Direction):
        pipe = self.pipe_map[pos]
        if pipe == 'S':
            return
        last_step_count = self.get_elem_in_dir(pos, from_dir)
        if last_step_count == 'S':
            last_step_count = 0
        step_count = last_step_count + 1
        self.pipe_map[pos] = step_count
        match pipe:
            case '|':
                if from_dir == Direction.UP:
                    return (pos + self.width, Direction.UP)
                elif from_dir == Direction.DOWN:
                    return (pos - self.width, Direction.DOWN)
                else:
                    raise Exception('Invalid direction')
            case '-':
                if from_dir == Direction.LEFT:
                    return (pos + 1, Direction.LEFT)
                elif from_dir == Direction.RIGHT:
                    return (pos - 1, Direction.RIGHT)
                else:
                    raise Exception('Invalid direction')
            case 'L':
                if from_dir == Direction.UP:
                    return (pos + 1, Direction.LEFT)
                elif from_dir == Direction.RIGHT:
                    return (pos - self.width, Direction.DOWN)
                else:
                    raise Exception('Invalid direction')
            case 'J':
                if from_dir == Direction.UP:
                    return (pos - 1, Direction.RIGHT)
                elif from_dir == Direction.LEFT:
                    return (pos - self.width, Direction.DOWN)
                else:
                    raise Exception('Invalid direction')
            case '7':
                if from_dir == Direction.DOWN:
                    return (pos - 1, Direction.RIGHT)
                elif from_dir == Direction.LEFT:
                    return (pos + self.width, Direction.UP)
                else:
                    raise Exception('Invalid direction')
            case 'F':
                if from_dir == Direction.DOWN:
                    return (pos + 1, Direction.LEFT)
                elif from_dir == Direction.RIGHT:
                    return (pos + self.width, Direction.UP)
                else:
                    raise Exception('Invalid direction')

    # Starting values are hard coded and need to be changed based on input
    def solve(self):
        start_pos = self.pipe_map.index('S')
        next = self.next_step_rec(start_pos + 1, Direction.LEFT)
        while next is not None:
            next = self.next_step_rec(next[0], next[1])

        cycle_steps = int(self.pipe_map[start_pos - 1])
        return math.ceil(cycle_steps / 2)
        




parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')
# sample answer should be 8

with open(abs_file_path) as file:
    lines = [line.strip() for line in file.readlines()]
    width = len(lines)
    pipe_map = PipeMap(list(''.join(lines)), width)
    ans1 = pipe_map.solve()
    print(ans1)
