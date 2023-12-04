import os
from pathlib import Path

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')

with open(abs_file_path) as file:
    pass
