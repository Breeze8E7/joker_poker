from base_classes import *
import math
from fractions import Fraction
from collections import Counter
from itertools import combinations

def present_odds(deck, hand_size=5):
    possible_hands = math.comb(deck.deck_size, hand_size)
    pair = 0
    two_pair = 0
    three_oak = 0
    straight = 0
    flush = 0
    full_house = 0
    four_oak = 0
    straight_flush = 0
    for hand in combinations(deck.deck_contents, hand_size):
        if is_straight_flush(hand):
            straight_flush +=1
            continue
        if is_four_oak(hand):
            four_oak +=1
            continue
        if is_full_house(hand):
            full_house +=1
            continue
        if is_flush(hand):
            flush +=1
            continue
        if is_straight(hand):
            straight +=1
            continue
        if is_three_oak(hand):
            three_oak +=1
            continue
        if is_two_pair(hand):
            two_pair +=1
            continue
        if is_pair(hand):
            pair +=1
    pair_odds = Fraction(pair, possible_hands)
    two_pair_odds = Fraction(two_pair, possible_hands)
    three_oak_odds = Fraction(three_oak, possible_hands)
    straight_odds = Fraction(straight, possible_hands)
    flush_odds = Fraction(flush, possible_hands)
    full_house_odds = Fraction(full_house, possible_hands)
    four_oak_odds = Fraction(four_oak, possible_hands)
    straight_flush_odds = Fraction(straight_flush, possible_hands)
    results = []
    results.append(f"The odds of a pair are {pair_odds}\n")
    results.append(f"The odds of a two pair are {two_pair_odds}\n")
    results.append(f"The odds of a three of a kind are {three_oak_odds}\n")
    results.append(f"The odds of a straight are {straight_odds}\n")
    results.append(f"The odds of a flush are {flush_odds}\n")
    results.append(f"The odds of a full house are {full_house_odds}\n")
    results.append(f"The odds of a four of a kind are {four_oak_odds}\n")
    results.append(f"The odds of a straight flush are {straight_flush_odds}\n")
    print (results)
    return results

def is_pair(hand):
    rank_counts = Counter(card.rank for card in hand)
    for count in rank_counts.values():
        if count == 2:
            return 1
    return 0

def is_two_pair(hand):
    rank_counts = Counter(card.rank for card in hand)
    pair_count = 0
    for count in rank_counts.values():
        if count == 2:
            pair_count += 1
    return 1 if pair_count == 2 else 0

def is_three_oak(hand):
    rank_counts = Counter(card.rank for card in hand)
    for count in rank_counts.values():
        if count == 3:
            return 1
    return 0

def is_four_oak(hand):
    rank_counts = Counter(card.rank for card in hand)
    for count in rank_counts.values():
        if count == 4:
            return 1
    return 0

def is_full_house(hand):
    rank_counts = Counter(card.rank for card in hand)
    has_three = False
    has_pair = False
    for count in rank_counts.values():
        if count == 3:
            has_three = True
        elif count == 2:
            has_pair = True
        if has_three and has_pair:
            return 1  
    return 0

def is_flush(hand):
    suit_counts = Counter(card.suit for card in hand)
    for count in suit_counts.values():
        if count == 5:
            return 1
    return 0

def is_straight(hand):
    unique_ranks = sorted(set(card.rank for card in hand))
    for i in range(len(unique_ranks) - 4):
        if unique_ranks[i:i+5] == list(range(unique_ranks[i], unique_ranks[i]+5)):
            return 1
    if set(unique_ranks) >= {1, 2, 3, 4, 5}:
        return 1
    return 0

def is_straight_flush(hand):
    return 1 if is_flush(hand) and is_straight(hand) else 0