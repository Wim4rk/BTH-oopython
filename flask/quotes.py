#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Quote gets quotes from a json-file and serves
them up for use in other apps.

JSON-file should be in format:

"Q1": "Quote..."
"Q2": "Quote..."
etc.
"""

import json
import random
import textwrap

class Quotes():
    """
    Serves up quotes
    """

    def __init__(self, file):
        self.get_quotes(file)

    def get_quotes(self, file):
        """Opens json-file, stores dictionary"""
        self.quotes = json.load(open(file, encoding="utf-8"))

    def random_quote(self):
        """Returns a random quote"""
        quotes_list = list(self.quotes.values())
        return textwrap.fill(random.choice(quotes_list))

    def print_random_quote(self):
        """
        Like it says, great for testing
        this class
        """
        print(self.random_quote())

if __name__ == "__main__":
    qu = Quotes('quotes.json')
    qu.print_random_quote()
