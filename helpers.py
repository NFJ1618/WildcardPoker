from collections import Counter
import poker
import itertools
import pandas as pd

class Helper:
    ordinal_mapping = {
        9: "Straight Flush",
        8: "Straight Flush",
        7: "Four of a Kind",
        6: "Full House",
        5: "Flush",
        4: "Straight",
        3: "Three of a Kind",
        2: "Two Pair",
        1: "One Pair",
        0: "High Card",
    }

    deck = list(range(52))
    
    joker_deck = list(range(53))
    
    init = False
    
    def create_csv(m, name):
        df = pd.DataFrame(list(m.items()), columns=['Hand', 'Poker_Hand_Type'])
        df = df.sort_values(by=['Poker_Hand_Type', 'Hand'])
        # print(df)
        # df.rows = ['1', '2', '3', '4', '5', '0']
        # df = df.sort_values()
        df.to_csv(name)




    def map_hand_data_to_tuple_and_type(data_line):
        suit_map = {1: 'h', 2: 's', 3: 'd', 4: 'c'}
        rank_map = {
            1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
            11: 'J', 12: 'Q', 13: 'K'
        }

        # Split the data line into individual attributes
        attributes = [int(x) for x in data_line.split(',')]
        
        # Parse the card attributes
        cards = [rank_map[attributes[i+1]] + suit_map[attributes[i]] for i in range(0, 10, 2)]
        hand_type = attributes[-1]  # The last number represents the type of poker hand

        return (tuple(cards), Helper.ordinal_mapping[hand_type])


    def generate_5_card_combinations(joker=False):
        if not Helper.init:
            Helper.create_card_mapping()
            Helper.init = True
        if joker:
            deck = Helper.joker_deck
        else:
            deck = Helper.deck
        for combination in itertools.combinations(deck, 5):
            yield combination

    def create_card_mapping():
        if Helper.init:
            return
        card_mapping = {}
        counter = 0
        card_mapping[52] = '*'
        for suit in list(poker.Suit):
            for rank in list(poker.Rank):
                card_mapping[counter] = rank.val + suit.value[1]
                counter += 1
        Helper.deck = [card_mapping[i] for i in Helper.deck]
        Helper.joker_deck = [card_mapping[i] for i in Helper.joker_deck]

    def is_straight(ranks):
        """Check if the hand is a straight."""
        if 12 in ranks:
            # Check for the low-Ace straight
            low_straight = set([12, 0, 1, 2, 3])
            if low_straight.issubset(set(ranks)):
                return True
        return len(set(ranks)) == 5 and max(ranks) - min(ranks) == 4

    def is_flush(suits):
        """Check if the hand is a flush."""
        return len(set(suits)) == 1
    
    def classify_poker_hand(hand):
        # Helper functions

        # Parse the hand
        ranks = sorted('23456789TJQKA'.index(rank) for rank, suit in hand)
        suits = [suit for rank, suit in hand]

        # Check for each type of hand
        if Helper.is_straight(ranks) and Helper.is_flush(suits):
            return "Straight Flush"
        if Counter(ranks).most_common(1)[0][1] == 4:
            return "Four of a Kind"
        if sorted(Counter(ranks).values()) == [2, 3]:
            return "Full House"
        if Helper.is_flush(suits):
            return "Flush"
        if Helper.is_straight(ranks):
            return "Straight"
        if Counter(ranks).most_common(1)[0][1] == 3:
            return "Three of a Kind"
        if sorted(Counter(ranks).values()) == [1, 2, 2]:
            return "Two Pair"
        if Counter(ranks).most_common(1)[0][1] == 2:
            return "One Pair"
        return "High Card"


    def classify_poker_hand_dup_helper(hand):
        ranks = sorted('23456789TJQKA'.index(rank) for rank, suit in hand)
        suits = [suit for rank, suit in hand]
        s = set()
        counter_ranks = Counter(ranks)
        counter_values = list(counter_ranks.values())
        # Check for each type of hand
        if 5 in counter_values:
            s.add('Five of a Kind')
        if Helper.is_straight(ranks) and Helper.is_flush(suits):
            s.add("Straight Flush")
        if 4 in counter_values:
            s.add("Four of a Kind")
            s.add('Three of a Kind')
            s.add('Two Pair')
            s.add('One Pair')
        if sorted(counter_values) == [2, 3]:
            s.add("Full House")
            s.add('Three of a Kind')
            s.add('Two Pair')
            s.add('One Pair')
        if Helper.is_flush(suits):
            s.add("Flush")
        if Helper.is_straight(ranks):
            s.add("Straight")
        if 3 in counter_values:
            s.add("Three of a Kind")
            s.add('One Pair')
        if counter_values.count(2) == 2:
            s.add("Two Pair")
            s.add('One Pair')
        if 2 in counter_values:
            s.add("One Pair")
        s.add("High Card")
        return s

    def classify_poker_hand_dup(hand):
        # Helper functions

        # Parse the hand
        
        if "*" in hand:
            s = set()
            deck = Helper.deck
            hand = [i for i in hand if i != '*']
            for i in deck:
                hand.append(i)
                s |= Helper.classify_poker_hand_dup_helper(hand)
                hand.pop()
            return s
            
        else:
            return Helper.classify_poker_hand_dup_helper(hand)