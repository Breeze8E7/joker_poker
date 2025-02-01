from enum import Enum

Rank = Enum("rank", ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"])
Suit = Enum("suit", ["heart", "diamond", "spade", "club"])

class Card:
    def __init__(self):
        self.titles = []
        self.ace_clubs = False
        self.two_clubs = False
        self.three_clubs = False
        self.four_clubs = False
        self.five_clubs = False
        self.six_clubs = False
        self.seven_clubs = False
        self.eight_clubs = False
        self.nine_clubs = False
        self.ten_clubs = False
        self.jack_clubs = False
        self.queen_clubs = False
        self.king_clubs = False
        self.ace_diamonds = False
        self.two_diamonds = False
        self.three_diamonds = False
        self.four_diamonds = False
        self.five_diamonds = False
        self.six_diamonds = False
        self.seven_diamonds = False
        self.eight_diamonds = False
        self.nine_diamonds = False
        self.ten_diamonds = False
        self.jack_diamonds = False
        self.queen_diamonds = False
        self.king_diamonds = False
        self.ace_hearts = False
        self.two_hearts = False
        self.three_hearts = False
        self.four_hearts = False
        self.five_hearts = False
        self.six_hearts = False
        self.seven_hearts = False
        self.eight_hearts = False
        self.nine_hearts = False
        self.ten_hearts = False
        self.jack_hearts = False
        self.queen_hearts = False
        self.king_hearts = False
        self.ace_spades = False
        self.two_spades = False
        self.three_spades = False
        self.four_spades = False
        self.five_spades = False
        self.six_spades = False
        self.seven_spades = False
        self.eight_spades = False
        self.nine_spades = False
        self.ten_spades = False
        self.jack_spades = False
        self.queen_spades = False
        self.king_spades = False
    
    def create_card(self, rank, suit):
        self.titles.append(f"{rank} of {suit}, ")
        match (rank, suit):
            case (Rank.ace, Suit.club):
                self.ace_clubs = True
            case (Rank.ace, Suit.heart):
                self.ace_hearts = True
            case (Rank.ace, Suit.spade):
                self.ace_spades = True
            case (Rank.ace, Suit.diamond):
                self.ace_diamonds = True
            case (Rank.two, Suit.club):
                self.two_clubs = True
            case (Rank.two, Suit.heart):
                self.two_hearts = True
            case (Rank.two, Suit.spade):
                self.two_spades = True
            case (Rank.two, Suit.diamond):
                self.two_diamonds = True
            case (Rank.three, Suit.club):
                self.three_clubs = True
            case (Rank.three, Suit.heart):
                self.three_hearts = True
            case (Rank.three, Suit.spade):
                self.three_spades = True
            case (Rank.three, Suit.diamond):
                self.three_diamonds = True
            case (Rank.four, Suit.club):
                self.four_clubs = True
            case (Rank.four, Suit.heart):
                self.four_hearts = True
            case (Rank.four, Suit.spade):
                self.four_spades = True
            case (Rank.four, Suit.diamond):
                self.four_diamonds = True
            case (Rank.five, Suit.club):
                self.five_clubs = True
            case (Rank.five, Suit.heart):
                self.five_hearts = True
            case (Rank.five, Suit.spade):
                self.five_spades = True
            case (Rank.five, Suit.diamond):
                self.five_diamonds = True
            case (Rank.six, Suit.club):
                self.six_clubs = True
            case (Rank.six, Suit.heart):
                self.six_hearts = True
            case (Rank.six, Suit.spade):
                self.six_spades = True
            case (Rank.six, Suit.diamond):
                self.six_diamonds = True
            case (Rank.seven, Suit.club):
                self.seven_clubs = True
            case (Rank.seven, Suit.heart):
                self.seven_hearts = True
            case (Rank.seven, Suit.spade):
                self.seven_spades = True
            case (Rank.seven, Suit.diamond):
                self.seven_diamonds = True
            case (Rank.eight, Suit.club):
                self.eight_clubs = True
            case (Rank.eight, Suit.heart):
                self.eight_hearts = True
            case (Rank.eight, Suit.spade):
                self.eight_spades = True
            case (Rank.eight, Suit.diamond):
                self.eight_diamonds = True
            case (Rank.nine, Suit.club):
                self.nine_clubs = True
            case (Rank.nine, Suit.heart):
                self.nine_hearts = True
            case (Rank.nine, Suit.spade):
                self.nine_spades = True
            case (Rank.nine, Suit.diamond):
                self.nine_diamonds = True
            case (Rank.ten, Suit.club):
                self.ten_clubs = True
            case (Rank.ten, Suit.heart):
                self.ten_hearts = True
            case (Rank.ten, Suit.spade):
                self.ten_spades = True
            case (Rank.ten, Suit.diamond):
                self.ten_diamonds = True
            case (Rank.jack, Suit.club):
                self.jack_clubs = True
            case (Rank.jack, Suit.heart):
                self.jack_hearts = True
            case (Rank.jack, Suit.spade):
                self.jack_spades = True
            case (Rank.jack, Suit.diamond):
                self.jack_diamonds = True
            case (Rank.queen, Suit.club):
                self.queen_clubs = True
            case (Rank.queen, Suit.heart):
                self.queen_hearts = True
            case (Rank.queen, Suit.spade):
                self.queen_spades = True
            case (Rank.queen, Suit.diamond):
                self.queen_diamonds = True
            case (Rank.king, Suit.club):
                self.king_clubs = True
            case (Rank.king, Suit.heart):
                self.king_hearts = True
            case (Rank.king, Suit.spade):
                self.king_spades = True
            case (Rank.king, Suit.diamond):
                self.king_diamonds = True
            case _:
                return "Invalid Card"    

class Deck:
    def __init__(self):
        self.deck_size = 52
        self.deck_contents = []
    
    def create_basic_deck(self):
        for x in Rank:
            for y in Suit:
                card = Card()
                card.create_card(x, y)
                self.deck_contents.append(card)

    def display_deck(self):
        for card in self.deck_contents:
            print(card.titles)