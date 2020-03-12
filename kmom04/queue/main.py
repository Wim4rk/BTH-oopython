#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Handle queue with a menu
"""

import sys
from queue import Queue

class Handler():
    """ Class handling menu etc """

    def __init__(self):
        self.line = Queue()
        self.menu = """Menu:
=======================================
<input>            Add value
1 - remove:        Remove next value
2 - peek:          See next value
3 - len:           Length of queue
4 - view           Show queue
5 - empty:         Queue is empty?
6 - help, menu:    Show menu
7 - exit, quit:    Quit the program
======================================="""

    def choice(self, inp):
        """ User request """
        str(inp.lower())

        if inp in ("1", "remove"):
            print("Removed:", self.line.dequeue())
        elif inp in ("2", "peek"):
            try:
                print("Next in line:", self.line.peek())
            except UnboundLocalError:
                print("List is empty")
        elif inp in ("3", "len"):
            print("Queue size:", self.line.size())
        elif inp in ("4", "view"):
            print("Queue:", self.line.view())
        elif inp in ("5", "empty"):
            print("Queue is empty:", self.line.is_empty())
        elif inp in ("6", "menu", "help"):
            self.show_menu()
        elif inp in ("7", "exit", "quit"):
            self.end_queue()
        else:
            self.line.enqueue(inp)


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
