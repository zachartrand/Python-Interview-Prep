#!/usr/bin/env python3
"""
Merge Sort

Implementation of Merge Sort in Python.
"""

from insertion_sort import insertion_sort as _insertion_sort


def main():
    from random import randrange

    unordered_list1 = [randrange(100, 1000) for n in range(8)]
    unordered_list2 = [randrange(100, 1000) for n in range(12)]
    unordered_list3 = [randrange(100, 1000) for n in range(24)]

    ordered_list1 = merge_sort(unordered_list1)
    ordered_list2 = merge_sort(unordered_list2)
    ordered_list3 = merge_sort(unordered_list3)

    print("List 1 (unsorted):")
    print(unordered_list1)
    print("List 1 (sorted")
    print(ordered_list1)
    print()
    print("List 2 (unsorted):")
    print(unordered_list2)
    print("List 2 (sorted")
    print(ordered_list2)
    print()
    print("List 3 (unsorted):")
    print(unordered_list3)
    print("List 3 (sorted")
    print(ordered_list3)
    print()


def merge_sort(items, *, threshold: int = 15):
    n = len(items)
    if n < 2:
        return items

    # Split the array into two halves.
    middle_index = n // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    # If the subarrays are small enough,
    # sort them with an insertion sort.
    if middle_index < threshold:
        # Insertion sort is in-place, so set the sorted variables to
        # the left and right splits, then use the insertion sort
        # function.
        left_sorted, right_sorted = left_split, right_split
        _insertion_sort(left_sorted)
        _insertion_sort(right_sorted)
    # Otherwise, use a merge sort for the subarrays.
    else:
        left_sorted = merge_sort(left_split)
        right_sorted = merge_sort(right_split)

    return _merge(left_sorted, right_sorted)


def merge_sort_old(items):
    n = len(items)
    if n < 2:
        return items

    # Split the array into two halves.
    middle_index = n // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return _merge(left_sorted, right_sorted)


def _merge(left, right):
    sorted = []
    while left and right:
        if left[0] < right[0]:
            sorted.append(left.pop(0))
        else:
            sorted.append(right.pop(0))

    if left:
        sorted.extend(left)
    if right:
        sorted.extend(right)

    return sorted


if __name__ == "__main__":
    main()
