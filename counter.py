import poker
import itertools
from helpers import *
import pandas as pd
import time

# Creating the generator
five_card_combinations = Helper.generate_5_card_combinations(joker=True)

# Displaying the first few combinations for demonstration
# first_combinations = [next(five_card_combinations) for _ in range(5)]

# print([(classify_poker_hand(i), i) for i in first_combinations])
d = {
    "Five of a Kind": 0,
    "Straight Flush": 0,
    "Four of a Kind": 0,
    "Full House": 0,
    "Flush": 0,
    "Straight": 0,
    "Three of a Kind": 0,
    "Two Pair": 0,
    "One Pair": 0,
    "High Card": 0,
}

m = {}


start = time.time()
for ind, val in enumerate(five_card_combinations):
    c = Helper.classify_poker_hand_dup(val)
    # if c == 'Straight Flush':
    for i in c:
        d[i] += 1
    # print(c, val)
    # if ind > 10000:
    #     break
print(d)
end = time.time()
print({end-start})
    
# create_csv(m, "mystraightflush.csv")


# {
#     'Straight Flush': 36,
#  'Four of a Kind': 624,
#  'Full House': 3744,
#  'Flush': 5112,
#  'Straight': 9180,
#  'Three of a Kind': 54912,
#  'Two Pair': 123552,
#  'One Pair': 1098240,
#  'High Card': 1303560
# }


# +1020
# -4
# -1020
