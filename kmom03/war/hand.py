#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Hand class represents a player

Hand ska representera en spelare. Vid start av spelet ska två Hand objekt
skapas och hälften av Card objekten från Deck ska delas ut till
vardera Hand objekt.
"""

from deck import Deck

class Hand():
    """ Class Hand represents a player """

    def __init__(self, name):
        """ Construct Hand-class """
        self.player_name = name
        self.hand = []

    def draw(self, deck):
        """ Draw a card from Deck """
        self.hand.append(deck.draw())
        return self


    def show_card(self):
        """ Show top card """
        return self.hand.pop(0)


    def show_hand(self):
        """ Show hand - the entire hand """
        for card in self.hand:
            print(card)

    def discard(self):
        """ Throw random card away """
        # Would need more logic...
        # Should be specified, won't use in 'war'
        return self.hand.pop()



if __name__ == "__main__":
    hand = Hand("Hannes")
    stack = Deck()
    stack.shuffle()
    hand.draw(stack).draw(stack)
    hand.show_hand()
