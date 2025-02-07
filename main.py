from deck_classes import *
from odds_recursive import *
from card_classes import *

def main():
    test_deck = Deck()
    test_deck.create_basic_deck()
    test_deck.display_deck()
    present_odds(test_deck)

if __name__ == "__main__":
    main()