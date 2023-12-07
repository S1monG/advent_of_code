import os
from pathlib import Path

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')

class Hand:
    def __init__(self, hand: str, bid: int):
        # replacing chars to make it easier to compare hands by
        # using pythons built in string comparison
        hand = hand.replace('A', 'E').replace('T', 'A').replace('J', 'B').replace('Q', 'C').replace('K', 'D')
        self.hand = hand
        self.bid = bid

    def get_bid(self) -> int:
        return self.bid
    
    def hand_strength(self) -> int:
        # char mapped to count
        l = {}
        for char in self.hand:
            l[char] = l.get(char, 0) + 1
        if len(l) == 1: # five of a kind
            return 6
        elif any(value == 4 for value in l.values()): # four of a kind
            return 5
        elif len(l) == 2 and any(value == 3 for value in l.values()): # full house
            return 4
        elif any(value == 3 for value in l.values()): # three of a kind
            return 3
        elif len(l) == 3: # two pairs
            return 2
        elif len(l) == 4: # one pair
            return 1
        else:
            return 0

    def __str__(self):
        return self.hand
    
    # implement the less than operator to sort the hands
    def __lt__(self, other):
        this_hand_strength = self.hand_strength()
        other_hand_strength = other.hand_strength()
        if this_hand_strength == other_hand_strength:
            return self.hand < other.hand
        else:
            return this_hand_strength < other_hand_strength

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
