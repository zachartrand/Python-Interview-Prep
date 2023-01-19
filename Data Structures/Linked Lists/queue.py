#!/usr/bin/env python3
"""
Queue Module
"""

__all__ = ["Queue"]

from node import Node


def main():
    print("Creating a deli line with up to 10 orders...\n------------")
    deli_line = Queue(10)
    print("Adding orders to our deli line...\n------------")
    deli_line.enqueue("egg and cheese on a roll")
    deli_line.enqueue("bacon, egg, and cheese on a roll")
    deli_line.enqueue("toasted sesame bagel with butter and jelly")
    deli_line.enqueue("toasted roll with butter")
    deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
    deli_line.enqueue("two fried eggs with home fries and ketchup")
    deli_line.enqueue("egg and cheese on a roll with jalapeos")
    deli_line.enqueue("plain bagel with plain cream cheese")
    deli_line.enqueue("blueberry muffin toasted with butter")
    deli_line.enqueue("bacon, egg, and cheese on a roll")
    deli_line.enqueue("western omelet with home fries")
    # ------------------------ #
    print("------------\nOur first order will be " + deli_line.peek())
    print("------------\nNow serving...\n------------")
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        if not self.has_space():
            print("Sorry, no more room!")
            return None

        item_to_add = Node(value)
        print(f"Adding {value} to the queue!")

        if self.is_empty():
            self.head = item_to_add
            self.tail = item_to_add
        else:
            self.tail.set_next_node(item_to_add)
            self.tail = item_to_add

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("The queue is totally empty!")
            return None

        item_to_remove = self.head
        value = item_to_remove.value
        print(f"Removing {value} from the queue!")

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = item_to_remove.next_node

        self.size -= 1

        return value

    def peek(self):
        if not self.is_empty():
            return self.head.value

        print("Nothing to see here!")
        return None

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size is None:
            return True

        return self.max_size > self.get_size()

    def is_empty(self):
        return self.size == 0


if __name__ == "__main__":
    main()
