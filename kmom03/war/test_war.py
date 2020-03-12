#!/usr/bin/env python3

""" Tests for war game """

import unittest

# import war
from hand import Hand
from card import Card
from deck import Deck
from war import War

class CheckCards(unittest.TestCase):
    """Tests for the card class"""

    game = War()
    deck = Deck()
    card = Card(0, "hearts")


    def test_suit_number(self):
        """ Test if a setup card returns class variables """
        self.card = Card(6, "clubs")
        # __repr__ returns face_value, wich is value + 1 and suit
        self.assertEqual(str(self.card), "7 of clubs")


    def test_card_draw(self):
        """ Make sure drawn card is not in deck (list) """
        self.deck = Deck()
        drawn = self.deck.draw()
        self.assertNotIn(drawn, self.deck.cards)


    # def test_for_jokers(self):
    #     """ Are there any jokers in the deck? """
    #     self.deck = Deck()
    #     self.deck.add_jokers(2)
    #     self.assertIn("joker of spades", str(self.deck.cards))

    def test_deck_shuffle(self):
        """ See if shuffling works """
        self.deck = Deck()
        stacked = self.deck.cards
        self.deck.shuffle()
        shuffled = self.deck
        self.assertNotEqual(stacked, shuffled)

    def test_deck_stacked(self):
        """ Check if stacking works - sanity check """
        self.deck = Deck()
        stacked = self.deck.cards
        self.assertEqual(stacked, self.deck.cards)

    def test_hands(self):
        """ Check no cards are mixed or duplicate """
        self.game = War()
        self.game.start_game()
        while len(self.game.player_1.hand) > 0:
            test_card = self.game.player_1.show_card()
            self.assertNotIn(test_card, self.game.player_2.hand)

    def test_count_hands(self):
        """ Are players hands equally big? """
        self.game = War()
        self.game.start_game()
        self.assertEqual(len(self.game.player_1.hand), len(self.game.player_2.hand))


# def test_fiftytwo(self):
#     """ See if deck contains 52 random cards """
#     pile = []
#     for c in deck
#         if c in pile:
#             # test failed
#             return False
#         else:
#             pile.append[c]
#     # Test successful
#     return True

    # def tearDown(self):
    #     self.card.dispose()



# Start by testing deck.py

if __name__ == "__main__":
    unittest.main()
