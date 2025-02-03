from enum import Enum
import random
from collections import Counter

Rank = Enum("rank", ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"])
Suit = Enum("suit", ["heart", "diamond", "spade", "club"])

class Card:
    def __init__(self, rank, suit, title):
        self.rank = rank
        self.suit = suit
        self.title = title

class Deck:
    def __init__(self):
        self.deck_size = 52
        self.deck_contents = []
        self.hand = []
        self.rank_counts = Counter()
        self.suit_counts = Counter()
    
    def create_basic_deck(self):
        for x in Rank:
            for y in Suit:
                title = f"{x} of {y}"
                card = Card(x, y, title)
                self.deck_contents.append(card)
                self.rank_counts[x] += 1
                self.suit_counts[y] += 1

    def display_deck(self):
        print ("Current deck:")
        for card in self.deck_contents:
            print(card.title)
        print("\nRank counts:", self.rank_counts)
        print("Suit counts:", self.suit_counts)

    def shuffle_deck(self):
        return random.shuffle(self.deck_contents)
    
    def draw_from_deck(self, int):
        current_hand = random.sample(self.deck_contents, int)
        print ("Current hand:")
        for card in current_hand:
            self.hand.append(card)
            self.deck_contents.remove(card)
        for card in self.hand:
            print (card.title)

    def reset_deck(self):
        self.deck_contents.extend(self.hand)
        self.hand.clear()
