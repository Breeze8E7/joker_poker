from base_classes import *
import math
from fractions import Fraction

"""
def template_odds(deck):
    x = #hand type# _combos_all(deck)
    y = base_combinations(deck)
    print (f"x = {x}, y = {y}")
    if y == 0:
        print("Error: No valid hands to calculate odds.")
        return None
    z = Fraction(x, y)
    print (f"The odds of a #hand type# are {z}")
    return z
"""


def base_combinations(deck, hand_size=5):
    d = deck.deck_size
    h = hand_size
    if d <= 0 or h <= 0:
        print ("No valid hands")
        return 0
    return math.comb(d, h)

## pair hands ##

def pair_odds(deck):
    x = pair_combos_all(deck)
    y = base_combinations(deck)
    print (f"x = {x}, y = {y}")
    if y == 0:
        print("Error: No valid hands to calculate odds.")
        return None
    z = Fraction(x, y)
    print (f"The odds of a pair are {z}")
    return z

def pair_combos_all(deck):
    count = 0
    for rank in Rank:
        count += pair_combos_rank(deck, rank.name)
    print (f"Possible pairs: {count}")
    return count

def pair_combos_rank(deck, rank_name):
    rank = Rank[rank_name]
    num_cards_in_rank = deck.rank_counts[rank]
    if num_cards_in_rank >= 2:
        print (f"Possible pairs of {rank_name}: {math.comb(num_cards_in_rank, 2)} ")
        pair_ways = math.comb(num_cards_in_rank, 2)
        remaining_cards = deck.deck_size - pair_ways
        
        
        return 
    return 0

## pair hands ##

def two_pair_combinations(deck):
    #math
    count = 0
    return count

def three_oak_combinations(deck):
    #math
    count = 0
    return count

def four_oak_combinations(deck):
    #math
    count = 0
    return count

def full_house_combinations(deck):
    #math
    count = 0
    return count

### flush hands ###

def flush_odds(deck):
    x = flush_combos_all(deck)
    y = base_combinations(deck)
    print (f"x = {x}, y = {y}")
    if y == 0:
        print("Error: No valid hands to calculate odds.")
        return None
    z = Fraction(x, y)
    print (f"The odds of a flush are {z}")
    return z

def flush_combos_all(deck):
    count = 0
    count += flush_combos_clubs(deck)
    count += flush_combos_diamonds(deck)
    count += flush_combos_hearts(deck)
    count += flush_combos_spades(deck)
    print (f"Possible total flushes: {count} ")
    return count

def flush_combos_clubs(deck):
    num_cards_in_suit = deck.suit_counts[Suit.club]
    if num_cards_in_suit >= 5:
        print (f"Possible club flushes: {math.comb(num_cards_in_suit, 5)} ")
        return math.comb(num_cards_in_suit, 5)
    return 0

def flush_combos_hearts(deck):
    num_cards_in_suit = deck.suit_counts[Suit.heart]
    if num_cards_in_suit >= 5:
        print (f"Possible heart flushes: {math.comb(num_cards_in_suit, 5)} ")
        return math.comb(num_cards_in_suit, 5)
    return 0

def flush_combos_spades(deck):
    num_cards_in_suit = deck.suit_counts[Suit.spade]
    if num_cards_in_suit >= 5:
        print (f"Possible spade flushes: {math.comb(num_cards_in_suit, 5)} ")
        return math.comb(num_cards_in_suit, 5)
    return 0

def flush_combos_diamonds(deck):
    num_cards_in_suit = deck.suit_counts[Suit.diamond]
    if num_cards_in_suit >= 5:
        print (f"Possible diamond flushes: {math.comb(num_cards_in_suit, 5)} ")
        return math.comb(num_cards_in_suit, 5)
    return 0

### flush hands ###

### straight hands ###

def straight_combinations(deck):
    #math
    count = 0
    return count