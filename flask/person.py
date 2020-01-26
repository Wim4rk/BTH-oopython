#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Person is a class to fetch personal data
for serving up to Flask-driven webpage.
"""

import json

class Person():
    """
    Contains data describing a person
    """

    firstName = ''
    lastName = ''
    birthDate = ''
    image = ''

    def __init__(self):
        self.get_person()

    def get_person(self):
        # json_data = json.load(open("olov.json", encoding="utf-8"))
        # firstName = json_data["firstN"]
        # lastName = json_data["lastN"]
        # birthDate = json_data["birthD"]
        # image = json_data["img"]

        self.firstName = 'Olov'
        self.lastName = 'Wimark'

    def print_name(self):
        print(self.firstName, " ", self.lastName)

if __name__ == "__main__":
    pn = Person()
    pn.print_name()
