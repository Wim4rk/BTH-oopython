#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Person is a class to fetch personal data
for serving up to Flask-driven webpage.
"""

import json

class Person(){
    """
    Contains data describing a person
    """

    def __init__(self):
        self.get_person()

    def get_person(self):
        json_data = json.load(open("olov.json", encoding="utf-8"))


}
