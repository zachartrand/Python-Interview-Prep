#!/usr/bin/env python3
"""
https://www.codecademy.com/code-challenges/code-challenge-reverse-a-singly-linked-list-python

Reverse a Singly-Linked List

Given the head of a linked list, write a function named

    reverse_linked_list(linked_list)

that reverses that linked list. Your function should return the head of
a new linked list where the values are in reverse order of the original
linked list. Additionally, your function should not modify the original
linked list.

For example, if your original linked list was

    4 -> 8 -> 15 -> None,

your function should return the head of the linked list

    15 -> 8 -> 4 -> None.

For this problem, you’ll be using our custom-built Node class.
The constructor for the node class is as follows:

    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node

The head of a linked list is a Node with some data whose next value
points to the next Node in the linked list.

This challenge was reported to have been asked at interviews with
Google and Amazon. If you’ve covered the material in Pass the Technical
Interview with Python or an equivalent, you should be able to solve
this challenge.
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def print_linked_list(self):
        value_list = [str(self.data)]
        current_node = self.next
        while current_node:
            value_list.append(str(current_node.data))
            current_node = current_node.next
        print(" -> ".join(value_list))
        print()


def main(linked_list):
    print("Original")
    demo_list = make_linked_list(linked_list)
    demo_list.print_linked_list()
    print("Reversed")
    reverse = reverse_linked_list(demo_list)
    reverse.print_linked_list()
    print("Original Unchanged")
    demo_list.print_linked_list()


def make_linked_list(array):
    last_node = None
    for value in reversed(array):
        current_node = Node(value, last_node)
        last_node = current_node

    return current_node


def reverse_linked_list(linked_list):
    # Write your code here
    current_node = linked_list
    new_node = None
    while current_node:
        new_node = Node(current_node.data, new_node)
        current_node = current_node.next

    return new_node


if __name__ == '__main__':
    main([4,8,15])
    print()
    main([2, 3, 5, 7, 11, 13, 17, 19])
