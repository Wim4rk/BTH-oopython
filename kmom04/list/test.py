#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" Tests for custom data structures """

# Gör tester
# Ta bort första sista och mitt i länkad lista

import unittest

from unorderedlist import UnorderedList
from error import KeyErr, ValErr, ScopeErr, ListEmpty

class TestLists(unittest.TestCase):
    """ Test class for lists """

    @classmethod
    def setUp(cls):
        cls.ul = UnorderedList()
        cls.ul.append(5)
        cls.ul.append(7)
        cls.ul.append(9)
        cls.ul.append(7)
        cls.ul.append(6)
        cls.ul.append("Last one")


    def test_erase(self):
        """ Try erasing list """

        self.ul.erase()

        with self.assertRaises(ListEmpty):
            self.ul.search(7)

        with self.assertRaises(ListEmpty):
            self.ul.print_list()

    def test_erase_empty(self):
        """ Erase an empty list """
        self.ul.erase()
        with self.assertRaises(ListEmpty):
            self.ul.erase()

    def test_delete_index(self):
        """ Delete single element, check return value """
        self.assertEqual(9, self.ul.remove_index(2))


    def test_delete_first(self):
        """ Try deleting first node in list """
        self.assertEqual(5, self.ul.remove_index(0))


    def test_delete_last(self):
        """ Try deleting last node in list """
        self.assertEqual("Last one", self.ul.remove_index(5))


    def test_delete_nonexistent(self):
        """ Delete a nonexistent node """
        with self.assertRaises(IndexError):
            self.ul.remove_index(22)


    def test_remove_value(self):
        """ Delete value """
        # Returns number of deleted items.
        self.assertEqual(2, self.ul.remove_value(7))


    def test_search(self):
        """ Quick test search """
        self.assertEqual(2, self.ul.search(9))
        with self.assertRaises(ValErr):
            self.ul.search(13)


    def test_get(self):
        """ Get value at index """
        self.assertEqual(7, self.ul.get(3))
        with self.assertRaises(KeyErr):
            self.ul.get(13)


if __name__ == "__main__":
    unittest.main()
