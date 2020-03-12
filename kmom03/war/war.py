#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Spelfunktionaliteten, spel loopen, ska hanteras i klassen War. Undvik att
lägga all kod i en metod, försök dela upp den i flera. Spelet ska starta
med python3 war.py.
"""

# I war (svälta räv) drar man ett kort i taget. När en spelare drar den färg som
# redan ligger vinner den spelare som har högst valör. Vinnaren tar alla kort på
# bordet. Seger inträffar när en spelare är helt utan kort.

import sys

from hand import Hand
from deck import Deck

class War():
    """ Class handling the game itself """

    def __init__(self):
        self.player_1 = Hand("Player 1")
        self.player_2 = Hand("Player 2")
        self.deck = Deck()
        self.pile = []
        self.menu = """Menu:
=======================================
exit, quit:    Quit the program
menu, help:    Show this menu
start:         Start the game
auto:          Run game automatically
======================================="""
        print(self.menu)

    def run_game(self, auto=False):
        """ Run the game """
        self.start_game()
        print("Enter for next hand")

        print('{0:20} {1}'.format("Player one", "Player two"))

        while len(self.player_1.hand) > 0 and len(self.player_2.hand) > 0:
            self.next_round(auto)

        print("============================================================")

        l_h1 = len(self.player_1.hand)
        l_h2 = len(self.player_2.hand)
        if  l_h2 < l_h1:
            print("{0:21}Player one wins!".format(" "))
        else:
            print("{0:21}Player two wins!".format(" "))

        print("{0:21}Player one: {1} cards".format(" ", l_h1))
        print("{0:21}Player two: {1} cards".format(" ", l_h2))
        print("{0:21}In pile: {1}".format(" ", len(self.pile)))


    def next_round(self, auto):
        """ Next round """
        p1_card = self.player_1.show_card()
        p2_card = self.player_2.show_card()

        self.pile.append(p1_card)
        self.pile.append(p2_card)

        res = "it's a draw"
        # large = ""

        if p1_card.suit == p2_card.suit:
            if p1_card.value > p2_card.value:
                res = "player 1 wins"
                self.player_1.hand += self.pile
                # large = len(self.player_1.hand)
            else:
                res = "player 2 wins"
                self.player_2.hand += self.pile
                # large = len(self.player_2.hand)
            self.pile = []

        if auto:
            (print('{0:20} {1:20} {2}'.format(str(p1_card),
                                              str(p2_card), res)))
        else:
            (input('{0:20} {1:20} {2}'.format(str(p1_card),
                                              str(p2_card), res)))


    def show_menu(self):
        """ Print the menu """
        # print(chr(27) + "[2J" + chr(27) + "[;H")
        print(self.menu)


    def choice(self, inp):
        """ User request """
        inp.lower()

        if inp in ("menu", "help"):
            print("Menu requested")
            self.show_menu()
        elif inp == "start":
            print("Start requested")
            self.run_game()
        elif inp == "auto":
            print("Game will run automatically")
            self.run_game(True)
        elif inp in ("exit", "quit"):
            print("Exit program")
            self.end_game()
        else:
            self.show_menu()


    def start_game(self):
        """ Set game up """
        self.deck.shuffle()
        # print("Deck shuffled")


        while len(self.deck.cards) > 0:
            self.player_1.draw(self.deck)
            self.player_2.draw(self.deck)

        # print("Deck has been shuffled and split")


    @classmethod
    def end_game(cls):
        """ End game in graceful manner """
        print("Done!")
        sys.exit()


if __name__ == "__main__":

    while True:
        GAME = War()
        GAME.choice(input("-->"))
        #GAME.choice("start")
