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
    rank_counts = Counter()
    for card in hand:
        if isinstance(card.rank, tuple):
            for rank in card.rank:
                rank_counts[rank.value] +=1
        else:
            rank_counts[card.rank] +=1
    for rank, count in rank_counts.items():
        if count == 2:
            return 1
    return 0

def is_two_pair(hand):
    rank_counts = Counter()
    joker_ranks = []
    for card in hand:
        if isinstance(card.rank, tuple):
            joker_ranks.append(card.rank)
        else:
            rank_counts[card.rank] +=1
    pairs = sum(1 for count in rank_counts.values() if count >= 2)
    for joker_rank_choices in combinations(joker_ranks, len(joker_ranks)):
        temp_counts = rank_counts.copy()
        for rank_tuple in joker_rank_choices:
            for possible_rank in rank_tuple:
                temp_counts[possible_rank.value] +=1
        if sum(1 for count in temp_counts.values() if count >= 2) >= 2:
            return 1
    return 0

def is_three_oak(hand):
    rank_counts = Counter()
    for card in hand:
        if isinstance(card.rank, tuple):
            for rank in card.rank:
                rank_counts[rank.value] +=1
        else:
            rank_counts[card.rank] +=1
    for rank, count in rank_counts.items():
        if count == 3:
            return 1
    return 0

def is_four_oak(hand):
    rank_counts = Counter()
    for card in hand:
        if isinstance(card.rank, tuple):
            for rank in card.rank:
                rank_counts[rank.value] +=1
        else:
            rank_counts[card.rank] +=1
    for rank, count in rank_counts.items():
        if count == 4:
            return 1
    return 0

def is_full_house(hand):
    rank_counts = Counter()
    joker_ranks = []
    for card in hand:
        if isinstance(card.rank, tuple):
            joker_ranks.append(card.rank)
        else:
            rank_counts[card.rank] += 1
    three_rank = None
    for rank, count in rank_counts.items():
        if count >= 3:
            three_rank = rank
    if three_rank:
        has_pair = any(count >= 2 for rank, count in rank_counts.items() if rank != three_rank)
        if has_pair:
            return 1
    for joker_rank_choices in combinations(joker_ranks, len(joker_ranks)):
        temp_counts = rank_counts.copy()
        for rank_tuple in joker_rank_choices:
            for possible_rank in rank_tuple:
                temp_counts[possible_rank.value] += 1
        three_rank = None
        for rank, count in temp_counts.items():
            if count >= 3:
                three_rank = rank
                break
        if three_rank:
            has_pair = any(count >= 2 for rank, count in temp_counts.items() if rank != three_rank)
            if has_pair:
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
    unique_ranks = set()
    joker_ranks = []
    for card in hand:
        if isinstance(card.rank, tuple):
            joker_ranks.append(card.rank)
        else:
            unique_ranks.add(card.rank)
    sorted_ranks = sorted(unique_ranks)
    for i in range(len(sorted_ranks) - 4):
        if sorted_ranks[i:i+5] == list(range(sorted_ranks[i], sorted_ranks[i]+5)):
            return 1
    if not joker_ranks:
        return 0
    for joker_rank_choices in combinations(joker_ranks, len(joker_ranks)):
        temp_ranks = unique_ranks.copy()
        for rank_tuple in joker_rank_choices:
            for possible_rank in rank_tuple:
                temp_ranks.add(possible_rank.value)
        sorted_ranks = sorted(temp_ranks)
        for i in range(len(sorted_ranks) - 4):
            if sorted_ranks[i:i+5] == list(range(sorted_ranks[i], sorted_ranks[i]+5)):
                return 1
    return 0

def is_straight_flush(hand):
    return 1 if is_flush(hand) and is_straight(hand) else 0

