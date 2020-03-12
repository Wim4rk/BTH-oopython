#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Class handling a queue data structure
"""

from node import Node

class Queue():
    """ Queue data structure class """

    def __init__(self):
        """Constructor"""
        self.head = None

    def is_empty(self):
        """ Return bool """
        return self.head is None

    def enqueue(self, item):
        """ Add item to list """
        current = self.head
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            return True

        while current.next is not None:
            current = current.next
        current.next = new_node

    def dequeue(self):
        """ Return first item in line """
        if self.head is None:
            return "Queue is empty"

        ret = self.head.data
        current = self.head
        self.head = current.next
        del current
        return ret

    def peek(self):
        """ Show front item without changing queue """
        if self.head is None:
            raise UnboundLocalError("List is empty")

        return self.head.data


    def view(self):
        """ Shows list, so long as it it relatively simple """
        l_str = ""
        if self.head is not None:
            current = self.head
            while current.next is not None:
                l_str += str(current.data) + " "
                current = current.next
            l_str += str(current.data) # Very easy to forget last value
        return l_str


    def size(self):
        """ Return length of queue """
        # return len(self.items)
        count = 0

        if self.head is not None:
            current = self.head
            while current.next is not None:
                count += 1
                current = current.next
            count += 1 # Add last node

        return count

if __name__ == "__main__":
    LINE = Queue()
    LINE.enqueue("One")
    LINE.enqueue(2)
    LINE.enqueue(3.0)
    LINE.enqueue("Four")

    print("Line size:", LINE.size())
    print("View:", LINE.view())
    print("First in line:", LINE.peek())
    print("Dequeue:", LINE.dequeue())
    print("Line size:", LINE.size())
    print("Line is empty?", LINE.is_empty())
