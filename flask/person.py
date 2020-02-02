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

    # firstName = ''
    # lastName = ''
    # birthDate = ''
    # image = ''

    def __init__(self, who):
        self.get_person(who)

    def get_person(self, who):
        file_name = who + ".json"
        json_data = json.load(open(file_name, encoding="utf-8"))
        self.firstName = json_data["firstN"]
        self.lastName = json_data["lastN"]
        self.name = self.firstName + " " + self.lastName
        self.school = json_data["school"]
        self._birthDate = json_data["birthD"]
        self.image = json_data["img"]

        #self.age = self.calculate_age()

    def calculate_age(self):
        born = datetime.strptime(self._birthDate, "%Y-%m-%d")
        today = datetime.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def get_image_link(self):
        return "/static/" + self.image

    def first_name(self):
        return self.firstName

    def school(self):
        return self.school

    def print_name(self):
        print(self.firstName, self.lastName)

    def print_age(self):
        print(self.calculate_age())

if __name__ == "__main__":
    pn = Person('olov')
    pn.print_name()
    pn.print_age()
