from deck_classes import *
from odds_recursive import *
from card_classes import *

def main():
    test_deck = Deck()
    test_deck.create_basic_deck()
    present_odds(test_deck)
    test_deck.upgrade_card("three", Suit.spade)
    test_deck.upgrade_card("three", Suit.diamond)
    test_deck.upgrade_card("three", Suit.heart)
    test_deck.upgrade_card("three", Suit.club)
    test_deck.upgrade_card("four", Suit.spade)
    test_deck.upgrade_card("four", Suit.club)
    test_deck.upgrade_card("four", Suit.heart)
    test_deck.upgrade_card("four", Suit.diamond)
    present_odds(test_deck)

if __name__ == "__main__":
    main()