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
    
    def get_next_pos(self, pos, from_dir: Direction):
        pipe = self.pipe_map[pos]
        # print(f'Pipe: {pipe}, from dir {from_dir}')
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
    
    def get_loop(self, start_pos, start_dir: Direction):
        positions = set()
        positions.add(start_pos)
        current_pos = (start_pos + 1, start_dir) # starting position is hardcoded and need to be changed based on input
        while current_pos[0] not in positions:
            positions.add(current_pos[0])
            current_pos = self.get_next_pos(current_pos[0], current_pos[1])
        return positions

    def solve(self) -> (int, int):
        start_pos = self.pipe_map.index('S')
        pipe_loop = self.get_loop(start_pos, Direction.LEFT) # Starting direction is hardcoded and need to be changed based on input
        ans1 = math.ceil(len(pipe_loop) / 2)

        # Go through each position, check intersections with the loop going diagonaly
        # Odd intersections => inside loop, even intersections => outside loop
        # Edge case if the pipe is a L or a 7
        ans2 = 0
        for idx in range(len(self.pipe_map)):
            if idx in pipe_loop:
                continue

            intersections = 0    
            i = idx
            while i < len(self.pipe_map):
                pipe = self.pipe_map[i]
                if i in pipe_loop and pipe != 'L' and pipe != '7':
                    intersections += 1
                i += self.width + 1
            
            if intersections % 2 == 1:
                ans2 += 1

        return ans1, ans2


    

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')

with open(abs_file_path) as file:
    lines = [line.strip() for line in file.readlines()]
    width = len(lines[0])
    pipe_map = PipeMap(list(''.join(lines)), width)
    ans1, ans2 = pipe_map.solve()
    print(f'Part 1: {ans1}')
    print(f'Part 2: {ans2}')
