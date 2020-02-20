#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Person is a class to fetch personal data
for serving up to Flask-driven webpage.
"""

import json
from datetime import datetime

class Person():
    """
    Contains data describing a person
    """

    # first_name = ''
    # last_name = ''
    # birthDate = ''
    # image = ''

    def __init__(self, who):
        """ Sets up the class """
        self.get_person(who)

    def get_person(self, who):
        """ Opens json file. """
        file_name = who + ".json"
        json_data = json.load(open(file_name, encoding="utf-8"))
        self.first_name = json_data["firstN"]
        self.last_name = json_data["lastN"]
        self.name = self.first_name + " " + self.last_name
        self.school = json_data["school"]
        self._birth_date = json_data["birthD"]
        self.image = json_data["img"]

        #self.age = self.calculate_age()

    def calculate_age(self):
        """ Sets persons age """
        born = datetime.strptime(self._birth_date, "%Y-%m-%d")
        today = datetime.today()
        return (today.year - born.year - ((today.month, today.day) <
                                          (born.month, born.day)))

    def get_image_link(self):
        """ Parses file name for images """
        return "static/" + self.image

    def print_name(self):
        """ Prints name """
        print(self.first_name, self.last_name)

    def print_age(self):
        """ Prints age """
        print(self.calculate_age())

if __name__ == "__main__":
    pn = Person('olov')
    pn.print_name()
    pn.print_age()
