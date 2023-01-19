#!/usr/bin/env python3
"""
Quicksort

Implementation of Quicksort in Python.
"""

__all__ = ["quicksort"]

from random import randint

from insertion_sort import insertion_sort_limits as _insertion_sort_limits


def main():
    from random import shuffle

    n = randint(6, 8)
    array = [i+1 for i in range(n)]
    array.append(randint(1, n-1))
    shuffle(array)

    quicksort_plus_print_statements(array)
    # print("Array sorted!")
    print("Post sort:", array)


def quicksort(array, /, start: int = 0, end: int = -1) -> None:
    if end == -1:
        end = len(array) - 1
        
    # This portion of array has been sorted.
    if start >= end:
        return
    
    # This block is for arrays of size 2. Needed to prevent infinite recursion.
    # elif end - start == 1:
    #     if array[end] < array[start]:
    #         array[start], array[end] = array[end], array[start]
    #     return

    # Select random element to be pivot.
    pivot_index = randint(start, end)
    pivot_element = array[pivot_index]
    # swap random element with last element in sub-arrays.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # tracks all elements which should be to left of (lesser than) pivot.
    less_than_pointer = start

    for i in range(start, end):
        item = array[i]
        if item <= pivot_element:
            # We found an element out of place
            # Swap element to the right-most portion of lesser elements.
            array[i], array[less_than_pointer] = array[less_than_pointer], array[i]

            # Tally that we have one more lesser element
            less_than_pointer += 1

    # Move pivot element to the right-most portion of lesser elements.
    array[end], array[less_than_pointer] = array[less_than_pointer], array[end]
    
    # Recursively sort left and right sub-arrays.
    quicksort(array, start, less_than_pointer - 1)
    quicksort(array, less_than_pointer + 1, end)


def quicksort_plus_insertion_sort(array, /, start: int = 0,
        end: int = -1, *, threshold: int = 64) -> None:
    """
    Implementation of Quicksort in Python.

    If the array given has 'threshold' items or fewer, this calls on an
    Insertion Sort function. For smaller arrays, Insertion Sort is
    quicker than Quicksort, and avoids picking a bad pivot.
    """
    if end == -1:
        end = len(array) - 1
    # this portion of array has been sorted
    if start >= end:
        return
    elif end - start <= threshold:
        _insertion_sort_limits(array, start, end + 1)
        return

    # select random element to be pivot
    pivot_index = randint(start, end)
    pivot_element = array[pivot_index]

    # swap random element with last element in sub-arrays
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # tracks all elements which should be to left of (lesser than) pivot
    less_than_pointer = start

    for i in range(start, end):
        # We found an element out of place
        if array[i] < pivot_element:
            # swap element to the right-most portion of lesser elements
            array[i], array[less_than_pointer] = array[less_than_pointer], array[i]
            # tally that we have one more lesser element
            less_than_pointer += 1

    # move pivot element to the right-most portion of lesser elements
    array[end], array[less_than_pointer] = array[less_than_pointer], array[end]

    # recursively sort left and right sub-arrays
    quicksort_plus_insertion_sort(array, start, less_than_pointer - 1)
    quicksort_plus_insertion_sort(array, less_than_pointer + 1, end)


def quicksort_plus_print_statements(array, /, start: int = 0, end: int = -1) -> None:
    if end == -1:
        end = len(array) - 1
    # this portion of array has been sorted
    if start >= end:
        return

    elif end - start == 1:
        print(f"Sorting {array[start: end + 1]}")
        if array[end] < array[start]:
            array[start], array[end] = array[end], array[start]
        
        print(f"Sorted: {array[start: end + 1]}")
        
        return

    print(f"Running quicksort on {array[start: end + 1]}")
    # select random element to be pivot
    pivot_index = randint(start, end)
    pivot_element = array[pivot_index]
    print(f"Selected pivot {pivot_element} at position "
          f"{pivot_index - start}")
    print(f"Swapping pivot ({pivot_element}) with end ({array[end]})")
    # swap random element with last element in sub-arrays
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # tracks all elements which should be to left of (lesser than) pivot
    less_than_pointer = start

    for i in range(start, end):
        # First conditional: we found an element out of place
        # Second conditional exists to prevent pivots that share a
        # value with another element from swapping positions, making
        # the sort stable.
        if array[i] <= pivot_element:
            # swap element to the right-most portion of lesser elements
            print(f"Swapping {array[i]} with {array[less_than_pointer]}")
            array[i], array[less_than_pointer] = array[less_than_pointer], array[i]

            # tally that we have one more lesser element
            less_than_pointer += 1

    # move pivot element to the right-most portion of lesser elements
    print(f"Swapping {array[less_than_pointer]} with {array[end]}")
    array[end], array[less_than_pointer] = array[less_than_pointer], array[end]
    print(f"{array[start: end + 1]} successfully partitioned")
    # recursively sort left and right sub-arrays

    quicksort_plus_print_statements(array, start, less_than_pointer - 1)
    quicksort_plus_print_statements(array, less_than_pointer + 1, end)


if __name__ == "__main__":
    main()
