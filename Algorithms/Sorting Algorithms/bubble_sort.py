#!/usr/bin/env python3
"""
Bubble Sort

A module that contains the Bubble Sort algorithm.

Here for educational purposes only. Do not use for serious 
programs. If you need to use an O(n^2) sorting algorithm, 
use Insertion Sort.
"""

__all__ = ["bubble_sort", "swap"]


def main():
    from random import randint, shuffle

    l = [i+1 for i in range(10)]
    l.append(randint(1, 11))
    shuffle(l)

    print("Unsorted:")
    print(l)
    print()

    bubble_sort(l)
    print()

    print("Sorted:")
    print(l)


def swap(array, index_1, index_2):
    """Swap two elements of an array at index_1 and index_2."""
    array[index_1], array[index_2] = array[index_2], array[index_1]


def bubble_sort(array):
    """
    Sort an array of values using the Bubble Sort algorithm.
    """
    n: int = len(array)
    is_sorted: bool = False
    swaps: int = 0
    comparisons: int = 0

    while not is_sorted:
        for i in range(n):
            is_sorted = True
            for j in range(n-i-1):
                if array[j] > array[j+1]:
                    swap(array, j, j+1)
                    is_sorted = False
                    swaps += 1

                comparisons += 1

            if is_sorted:
                break

    print("Bubble Sort Stats")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")


if __name__ == "__main__":
    main()
