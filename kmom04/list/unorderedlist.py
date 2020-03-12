#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Module contains class for handling node
"""

from node import Node
from error import KeyErr, ValErr, ListEmpty

class UnorderedList():
    """
    List class
    """

    def __init__(self):
        """ Initialize and set head to None - empty list."""
        self.head = None


    def append(self, value):
        """ Add a node last in list. """
        current = self.head
        new_node = Node(value)

        if self.empty_list():
            self.head = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node


    def set(self, index, data):
        """ Set value at index """
        if not self.empty_list():
            current_node = self.head
            counter = 0
            while current_node.next is not None and counter < index:
                current_node = current_node.next
                counter += 1
            if counter == index:
                current_node.data = data
                return

            raise KeyErr("Index not in list")

        raise ListEmpty("List is empty")


    def size(self):
        """ Return size - len - of list """

        if not self.empty_list():
            current = self.head
            count = 0
            while current.next is not None:
                count += 1
                current = current.next
            count += 1 # Addin last node

        return count


    def get(self, index):
        """ Get value by index """
        if not self.empty_list():
            current_node = self.head
            counter = 0
            while current_node.next is not None and counter < index:
                current_node = current_node.next
                counter += 1
            if counter == index:
                return current_node.data

            raise KeyErr("Index not in list")

        raise ListEmpty("List is empty")


    def search(self, value):
        """ Traverse list, search for value. Return integer for index"""
        if not self.empty_list():
            current = self.head
            counter = 0
            while current.next is not None:
                if current.data == value:
                    # print("Value: ", value)
                    return counter
                counter += 1
                current = current.next

            if current.data == value: # Allways the last node on its own.
                return counter

            raise ValErr("Search value not in list")

        raise ListEmpty("List is empty")


    def remove_index(self, index):
        """
        Delete single node at index
        Returns deleted value
        """
        if self.empty_list():
            raise ListEmpty("List is empty")

        current = self.head
        ret = None

        previous = None
        counter = 0
        while current is not None:
            ret = current.data
            if counter == index:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return ret

            previous = current
            current = current.next
            counter += 1

        raise IndexError("Index out of bounds, too high")


    def remove_value(self, value):
        """ Remove all instances of value """
        # Get index(es)
        counter = 0
        while True:
            try:
                index = self.search(value)
            except ListEmpty:
                raise ListEmpty("Can't search empty list")
            except ValErr:
                # Value not in list. We could be done,
                # or nothing was done.
                return counter

            # So now we know the index is there.
            self.remove_index(index)
            counter += 1


    def print_list(self):
        """ Shows list, so long as it it relatively simple """
        l_str = ""
        if not self.empty_list():
            current = self.head
            while current.next is not None:
                l_str += str(current.data) + " "
                current = current.next
            l_str += str(current.data) # Very easy to forget last value
            return l_str

        raise ListEmpty("List is empty")


    def empty_list(self):
        """ Return bool """
        return self.head is None


    def erase(self):
        """ Erase entire list """
        # What if someone tries to erase an empty list?
        if self.empty_list():
            raise ListEmpty("List is empty")
        current = self.head
        while current.next is not None:
            nxt = current.next
            self.remove_index(0) # Always delete first node
            current = nxt
        self.remove_index(0)
        return True

    def list_len(self):
        """ Length of list """
        count = 0

        if not self.empty_list():
            current = self.head
            while current.next is not None:
                count += 1
                current = current.next
            count += 1 # Adding last node

        return count


if __name__ == "__main__":
    LL = UnorderedList()
    LL.append(5)
    LL.append(7)
    LL.append(9)
    LL.append(7)
    LL.append(6)
    LL.append("Last one")

    try:
        LL.remove_index(6)
    except IndexError as index_error:
        print("Remove:", index_error)

    print("Search 7:", LL.search(7))
    print("Get 3:", LL.get(3))
    LL.set(3, "Three")
    print("Get 3:", LL.get(3))

    try:
        print(LL.search(3))
    except ValErr as val_err:
        print(val_err)

    print(LL.print_list())
    try:
        LL.remove_index(4)
    except ListEmpty as l_e:
        print(l_e)
    except IndexError as index_error:
        print(index_error)
    print(LL.print_list())
    LL.set(3, "Change me!")
    print(LL.print_list())

    LL.remove_value("Change me!")
    print(LL.print_list())
