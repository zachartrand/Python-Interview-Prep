"""Module for the Stack class."""

from node import Node


class Stack:
    def __init__(self, name, limit=1000):
        self.size = 0
        self.top_item = None
        self.limit = limit
        self.name = name

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("No more room!")
            raise OverflowError

    def pop(self):
        if self.is_not_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1

            return item_to_remove.value

        print("This stack is totally empty.")

    def peek(self):
        if self.is_not_empty():
            return self.top_item.value

        print("Nothing to see here!")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

    def is_not_empty(self):
        return self.size > 0

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def print_items(self):
        pointer = self.top_item
        print_list = []
        while pointer:
            print_list.append(pointer.value + 1)
            pointer = pointer.get_next_node()

        print_list.reverse()
        print(f"{self.get_name()} Stack: {print_list}")
