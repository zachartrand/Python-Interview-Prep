#!/usr/bin/env python3

from random import shuffle

from quicksort import quicksort, quicksort_plus_insertion_sort


def main():
    l = [i+1 for i in range(32)]
    shuffle(l)
    print("Unsorted:")
    print(l)
    print()

    l1, l2 = l[:], l[:]
    quicksort(l1)
    print("Sorted with Quicksort:")
    print(l1)

    quicksort_plus_insertion_sort(l2)
    print("Sorted with Quicksort and Insertion Sort:")
    print(l2)


if __name__ == "__main__":
    main()