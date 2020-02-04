#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Contains classes for lab1
"""

# from datetime import datetime
# import time

class Cat():
    """
    Lab1
    """

    _lives_left = 9
    nr_of_paws = 4

    def __init__(self):
        """ Awaken the c-c-cat... """
        self.eye_color = ''
        self.name = ''
        self._lives_left = -1

    def set_lives_left(self, num):
        """ Boost yout kitten """
        self._lives_left = num

    def get_lives_left(self):
        """ Before the kitty gets it! """
        return self._lives_left

    def description(self):
        """ How adorable! """
        return ("My cats name is " + self.name +
                ", has " + self.eye_color + " eyes and " +
                str(self._lives_left) + " lives left to live.")

class Duration():
    """
    Or durata
    """

    def __init__(self, H, m, s):
        """ Constructor """
        self.hours = H
        self.minutes = m
        self.seconds = s

    def __add__(self, other):
        """ Overloading (+) """
        s = (self.duration_to_sec(self.display()) +
             other.duration_to_sec(other.display()))
        return s

    def __iadd__(self, other):
        """ Overloading (+=) """
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds

        return self

    def display(self):
        """ Display duration as formatted string """
        t = []
        t.append(str(self.hours).zfill(2))
        t.append(str(self.minutes).zfill(2))
        t.append(str(self.seconds).zfill(2))

        return "-".join(t)

    @staticmethod
    def duration_to_sec(in_time):
        """ Converts given time into seconds """
        hours, minutes, seconds = map(int, in_time.split("-"))

        s = hours * 3600
        s += minutes * 60
        s += seconds

        return s

if __name__ == "__main__":
#     t = Duration(12, 14, 26)
#     print(t.display())
    print(Duration.duration_to_sec("40-40-40"))
