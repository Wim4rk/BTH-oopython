#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Card ska innehålla valör och färg. __repr__ ska överskuggas och returnera
en sträng med objekts tillstånd (värden, beskrivning av kortet).
"""

class Card():
    """
    Class resprents a card
    """
    def __init__(self, val, suit):
        self.suit = suit
        self.value = val
        self.face_value = self.value
        self.re_represent()


    def __repr__(self):
        """ Formal representation of card """
        return "{} of {}".format(self.face_value, self.suit)


    def re_represent(self):
        """ Set face value """
        if self.value in range(1, 9):
            self.face_value = str(self.value + 1)
        elif self.value == 10:
            self.face_value = "jack"
        elif self.value == 11:
            self.face_value = "queen"
        elif self.value == 12:
            self.face_value = "king"
        elif self.value == 13:
            self.face_value = "ace"
        elif self.value == 0:
            self.face_value = "joker"
