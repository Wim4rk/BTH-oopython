#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Handle queue with a menu
"""

import sys
from unorderedlist import UnorderedList
from error import ListEmpty, ValErr

class Handler():
    """ Class handling menu etc """

    def __init__(self):
        self.list = UnorderedList()
        self.menu = """Menu:
=======================================
<input>            Add value
1 - add:           Add number or menu keyword
2 - remove:        Remove value
3 - re_index       Remove index
4 - len:           Length of list
5 - view           Show list
6 - search:        Value index
7 - empty:         List is empty?
8 - help, menu:    Show menu
9 - exit, quit:    Quit the program
======================================="""

    #pylint:disable=too-many-branches
    def choice(self, inp):
        """ User request """
        str(inp.lower())

        if inp in ("1", "add"):
            app_value = input("Value to append: ")
            print("Appended:", self.list.append(app_value))
        elif inp in ("2", "remove"):
            rem_value = input("Value to remove: ")
            num_removed = self.list.remove_value(rem_value)
            if num_removed == 0:
                print("No such value in list")
            else:
                print("Removed:", num_removed,
                      "instances.")

        elif inp in ("3", "re_index"):
            try:
                rem_index = int(input("Index to remove:"))
                print("Removed: ", self.list.remove_index(rem_index))
            except TypeError:
                print("Input integer only")
            except IndexError:
                print("Index not in list")

        elif inp in ("4", "len"):
            print("List size:", self.list.list_len())

        elif inp in ("5", "view"):
            try:
                print("List:", self.list.print_list())
            except ListEmpty:
                print("List is empty")

        elif inp in ("6", "search"):
            val = input("Value to search for: ")
            try:
                print("Index of", val, ":", self.list.search(val))
            except ValErr:
                print("Value not in list")
            except ListEmpty:
                print("List is empty")

        elif inp in ("7", "empty"):
            print("List empty:", self.list.empty_list())

        elif inp in ("8", "menu", "help"):
            self.show_menu()

        elif inp in ("9", "exit", "quit"):
            self.end_queue()

        else:
            self.list.append(inp)

    def show_menu(self):
        """ Show the menu """
        print(self.menu)


    @classmethod
    def end_queue(cls):
        """ End game in graceful manner """
        print("Done!")
        sys.exit()

if __name__ == "__main__":

    FLOW = Handler()
    FLOW.show_menu()
    while True:
        FLOW.choice(input(">"))
