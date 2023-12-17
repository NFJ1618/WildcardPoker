from helpers import *
import pandas as pd

m= {}


with open('data/poker-hand-testing.data', 'r') as f:
    for ind, line in enumerate(f):
        cards, ord = map_hand_data_to_tuple_and_type(line.strip())
        m [cards] = ord
        # if ind > 10:
        #     break
        
create_csv(m, "testhands.csv")

