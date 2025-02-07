from enum import Enum
import random
from collections import Counter
from card_classes import *

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
                title = "Basic"
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

    def remove_card(self, rank_name, suit):
        rank = Rank[rank_name].value
        for card in self.deck_contents[:]:
            if card.rank == rank and card.suit == suit and card.title == "Basic":
                self.deck_contents.remove(card)
                self.deck_size -= 1
                self.rank_counts[Rank(rank)] -= 1
                self.suit_counts[suit] -= 1
                print(f"Successfully removed: {card.rank} of {card.suit}")
                return
        print(f"Card {rank_name} of {suit} not found!")

    def upgrade_card(self, rank_name, suit):
        self.remove_card(rank_name, suit)
        self.add_jackson_five(suit)

    def add_wild_joker(self, rank_name):
        rank = Rank[rank_name].value
        new_joker = Wild_Joker(rank)
        self.deck_contents.append(new_joker)
        self.deck_size +=1
        self.rank_counts[Rank(rank)] +=1
        for suit in Suit:
            self.suit_counts[suit] += 1
        print(f"Successfully added: Wild {rank}")

    def add_jackson_five(self, suit):
        new_joker = Jackson_Five(suit)
        self.deck_contents.append(new_joker)
        self.deck_size +=1
        self.suit_counts[suit] +=1
        for rank in new_joker.rank:
            self.rank_counts[rank.value] +=1
        print(f"Successfully added Jackson Five of {suit}")