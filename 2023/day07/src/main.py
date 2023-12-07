import os
from pathlib import Path

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/sample.txt')

class Hand:
    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid

    def get_bid(self) -> int:
        return self.bid

    def __str__(self):
        return self.hand
    
    # implement the less than operator to sort the hands
    def __lt__(self, other):
        return self.hand < other.hand

with open(abs_file_path) as file:
    # list of Hand objekts
    hand_list = []
    for line in file:
        hand, bid = line.split()
        hand_list.append(Hand(hand, bid))

    ans1 = 0
    hand_list.sort()
    for i in range(len(hand_list)):
        ans1 += int(hand_list[i].get_bid()) * (i + 1)

    print(f'Part 1: {ans1}')
