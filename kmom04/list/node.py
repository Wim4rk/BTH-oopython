#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Module contains class for handling node
"""

class Node: # pylint: disable=too-few-public-methods
    """
    Node class
    """

    def __init__(self, data, nxt=None):
        """
        Initialize object with data and set next to None
        """
        self.data = data
        self.next = nxt
