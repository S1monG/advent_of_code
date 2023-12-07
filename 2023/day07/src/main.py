import os
from pathlib import Path

parent_dir = Path(os.path.dirname(__file__)).parent
abs_file_path = os.path.join(parent_dir, 'data/input.txt')

def get_map_from_hand(hand: str):
    jokers = 0
    l = {}
    for char in hand:
        if char == '1':
            jokers += 1
        else:
            l[char] = l.get(char, 0) + 1
    return l, jokers

class Hand:
    def __init__(self, hand: str, bid: int):
        # replacing chars to make it easier to compare hands by
        # using pythons built in string comparison
        hand = hand.replace('A', 'D').replace('T', 'A').replace('J', '1').replace('Q', 'B').replace('K', 'C')
        self.hand = hand
        self.bid = bid

    def get_bid(self) -> int:
        return self.bid
    
    def hand_strength(self) -> int:
        # char mapped to count
        l, jokers = get_map_from_hand(self.hand)
        # sort the list by count, the first element will be the most common
        # if a hand only contains one type of card, the list will only contain one element
        # jokers (1) are not counted
        l = sorted(list(l.values()), reverse=True)

        if jokers == 5 or l[0] + jokers == 5: # five of a kind
            return 6
        elif l[0] + jokers == 4: # four of a kind
            return 5
        elif l[0] + jokers == 3 and l[1] == 2 or\
             l[0] + jokers == 2 and l[1] == 3: # full house
            return 4
        elif l[0]+ jokers == 3: # three of a kind
            return 3
        elif l[0] + jokers == 2 and l[1] == 2 or\
             l[0] == 2 and l[1] + jokers == 2: # two pairs
            return 2
        elif l[0] + jokers == 2: # one pair
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

    print(f'Part 2: {ans1}')
