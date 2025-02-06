from enum import Enum
import random
from collections import Counter

Suit = Enum("suit", ["heart", "diamond", "spade", "club"])
Rank = Enum("rank", {
    "ace": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "jack": 11,
    "queen": 12,
    "king": 13
})


class Card:
    def __init__(self, rank, suit, title=None):
        self.rank = rank.value
        self.suit = suit
        self.title = title

class Wild_Joker(Card):
    def __init__(self, rank, title="Joker"):
        self.rank = rank
        self.suit = (Suit.club, Suit.diamond, Suit.heart, Suit.spade)
        self.title = title