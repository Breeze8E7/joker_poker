from base_classes import *
from odds_calculators import *

def main():
    test_deck = Deck()
    test_deck.create_basic_deck()
    test_deck.draw_from_deck(5)
    test_deck.reset_deck()
    odds(test_deck)

if __name__ == "__main__":
    main()