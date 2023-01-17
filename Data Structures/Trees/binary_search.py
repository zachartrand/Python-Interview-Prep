#!/usr/bin/env python3
"""Module for the Binary Search Algorithm."""

__all__ = ["binary_search"]


def main():
    # test cases
    array = [5,6,7,8,9]
    print(f"Array: {array}")
    searches = [9, 10, 8, 4, 6]
    for search in searches:
        print(f"Searching for {search}...")
        print(f"Result: {binary_search(array, search)}")
        print()


def binary_search(sorted_list, target):
    """
    Return the index of the target value in the sorted_list if it
    exists. Otherwise, return -1.

    Parameters:
        sorted_list (Iterable): A list of values sorted from smallest
            to largest.

        target: The target value to find in the list.

    Returns:
        int: The index of the target value. If the target
            value is not found in the list, return -1.
    """
    left_pointer = 0
    right_pointer = len(sorted_list)

    # fill in the condition for the while loop
    while left_pointer < right_pointer:
        # calculate the middle index using the two pointers
        mid_index = left_pointer + (right_pointer - left_pointer) // 2
        mid_value = sorted_list[mid_index]
        if mid_value == target:
            return mid_index
        elif target < mid_value:
            # set the right_pointer to the appropriate value
            right_pointer = mid_index
        else:
            # set the left_pointer to the appropriate value
            left_pointer = mid_index + 1

    return -1


def binary_search_recursive_with_copies(sorted_list, target):
    """
    Return the index of the target value in the sorted_list if it
    exists. Otherwise, return -1.

    This version looks through smaller copies of the sorted_list, which
    is a wasteful use of memory. This is kept here for educational
    purposes only.
    """
    if (not sorted_list or target > sorted_list[-1]):
        return -1

    mid_index = len(sorted_list)//2
    mid_value = sorted_list[mid_index]
    if mid_value == target:
        return mid_index
    elif mid_value > target:
        left_half = sorted_list[:mid_index]
        return binary_search(left_half, target)
    else:
        right_half = sorted_list[mid_index + 1:]
        result = binary_search(right_half, target)
        if isinstance(result, str):
            return result

        return (result + mid_index + 1)


def binary_search_recursive(sorted_list, left_pointer,
                            right_pointer, target):
    """
    Return the index of the target value in the sorted_list if it
    exists. Otherwise, return -1.

    This is the recursive version of the binary search algorithm.
    It is slower than the iterative version used above. This is kept
    here for educational purposes only.
    """
    # this condition indicates we've reached an empty "sub-list"
    if left_pointer >= right_pointer:
        return -1

    # We calculate the middle index from the pointers now
    mid_index = (left_pointer + right_pointer) // 2
    mid_value = sorted_list[mid_index]

    if mid_value == target:
        return mid_index
    if mid_value > target:
        # we reduce the sub-list by passing in a new right_pointer
        return binary_search(sorted_list, left_pointer, mid_index, target)
    if mid_value < target:
        # we reduce the sub-list by passing in a new left_pointer
        return binary_search(sorted_list, mid_index + 1, right_pointer, target)


if __name__ == "__main__":
    main()
