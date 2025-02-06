from base_classes import *
from odds_recursive import *
from jokers import *

def main():
    test_deck = Deck()
    test_deck.create_basic_deck()
    test_deck.remove_card("three", Suit.spade)
    test_deck.remove_card("four", Suit.club)
    test_deck.display_deck()

if __name__ == "__main__":
    main()