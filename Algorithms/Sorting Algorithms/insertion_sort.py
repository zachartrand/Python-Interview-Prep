#!/usr/bin/env python3
"""
Insertion Sort module for Python

Implementation of the Insertion Sort algorithm in Python.
"""

__all__ = ["insertion_sort", "insertion_sort_limits"]


def main():
    from random import shuffle

    l = [i+1 for i in range(16)]
    shuffle(l)
    print("Unsorted array:")
    print(l, "\n")

    insertion_sort(l)

    print("Sorted array:")
    print(l)


def insertion_sort(array):
    n: int = len(array)
    if n < 2:
        return

    for i in range(1, n):
        key = array[i]
        j: int = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key


def insertion_sort_limits(array, /, start: int = 0, end: int = -1):
    if end == -1:
        end = len(array)
    n: int = end - start
    if n < 2:
        return

    for i in range(start + 1, end):
        key = array[i]
        j: int = i - 1
        while j >= start and key < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key


if __name__ == "__main__":
    main()
