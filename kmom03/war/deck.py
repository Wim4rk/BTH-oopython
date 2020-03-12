#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" Module holds the Deck class """

# Deck skall hålla en lista med 52 kort,
# det skall finnas en metod för att blanda korten

#pylint:disable=C0103

import random

from card import Card

class Deck():
    """ Class represents a deck of cards """
    def __init__(self):
        self.cards = []
        self.stack_deck()


    def stack_deck(self):
        """ Stack the deck """
        for suit in ["spades", "clubs", "diamonds", "hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))
                # print("{} of {}".format(value, suit))


    # def add_jokers(self, number):
    #     """ Add joker cards """
    #     if number > 4:
    #         number = 4

        # for i in range(1, number):
        #     for j in ["spades", "clubs", "diamonds", "hearts"]:
        #         self.cards.append(Card(0, j))
        #         # Does one give jokers a suit?


    def show(self):
        """ Show a deck of cards """
        for c in self.cards:
            print(c)


    def shuffle(self):
        """ Randomize card order in deck """
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


    def draw(self):
        """ Return one card from list of random cards """
        return self.cards.pop()


if __name__ == "__main__":
    deck = Deck()
    deck.show()
    deck.shuffle()
    print("=== Drawn cards ===")
    print(deck.draw())
    print(deck.draw())
    print(deck.draw())
    print(deck.draw())
