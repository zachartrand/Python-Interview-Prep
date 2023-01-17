#!/usr/bin/env python3
"""Module to test the sort method of the LinkedList class."""

from random import shuffle

from linked_list import LinkedList

l = [i+1 for i in range(16)]
shuffle(l)

ll1, ll2 = LinkedList(), LinkedList()
for n in reversed(l):
    ll1.insert_beginning(n)
    ll2.insert_beginning(n)

print()
print("Unsorted Linked List:")
print(ll1.stringify_list())
print()
ll1.sort()
print("Sorted Linked List Ascending:")
print(ll1.stringify_list())
print()

ll2.sort("descending")
print("Sorted Linked List Descending:")
print(ll2.stringify_list())
