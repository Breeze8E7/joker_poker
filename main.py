from base_classes import *
from odds_recursive import *

def main():
    test_deck = Deck()
    test_deck.create_basic_deck()
    present_odds(test_deck, 5)

if __name__ == "__main__":
    main()