from deck_classes import *
from card_classes import *
import math
from fractions import Fraction
from collections import Counter
from itertools import combinations

def present_odds(deck, hand_size=5):
    possible_hands = math.comb(deck.deck_size, hand_size)
    hand_counts = {
        "straight_flush": 0, "four_oak": 0, "full_house": 0,
        "flush": 0, "straight": 0, "three_oak": 0,
        "two_pair": 0, "pair": 0
    }
    for hand in combinations(deck.deck_contents, hand_size):
        if is_straight_flush(hand):
            hand_counts["straight_flush"] += 1
            continue
        if is_four_oak(hand):
            hand_counts["four_oak"] += 1
            continue
        if is_full_house(hand):
            hand_counts["full_house"] += 1
            continue
        if is_flush(hand):
            hand_counts["flush"] += 1
            continue
        if is_straight(hand):
            hand_counts["straight"] += 1
            continue
        if is_three_oak(hand):
            hand_counts["three_oak"] += 1
            continue
        if is_two_pair(hand):
            hand_counts["two_pair"] += 1
            continue
        if is_pair(hand):
            hand_counts["pair"] += 1
    results = []
    for hand_type, count in hand_counts.items():
        odds_fraction = Fraction(count, possible_hands)
        odds_percent = (count / possible_hands) * 100
        results.append(f"The odds of a {hand_type.replace('_', ' ')} are {odds_fraction}, or {odds_percent:.3f}%")
    print("\n".join(results))
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
    suit_counts = Counter()
    for card in hand:
        if isinstance(card.suit, tuple):
            for suit in card.suit:
                suit_counts[suit] +=1
        else:
            suit_counts[card.suit] +=1
    for suit, count in suit_counts.items():
        if count >= 5:
            return 1
    return 0

def is_straight(hand):
    unique_ranks = sorted(set(card.rank for card in hand))
    for i in range(len(unique_ranks) - 4):
        if unique_ranks[i:i+5] == list(range(unique_ranks[i], unique_ranks[i]+5)):
            return 1
    if set(unique_ranks) >= {1, 2, 3, 4, 5} or set(unique_ranks) >= {10, 11, 12, 13, 1}:
        return 1
    return 0

def is_straight_flush(hand):
    return 1 if is_flush(hand) and is_straight(hand) else 0

