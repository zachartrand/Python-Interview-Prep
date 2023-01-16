#!/usr/bin/env python3
"""
This module contains a solution to the Capturing Rainwater Problem in
Python.

From the Pass the Technical Interview with Python Skill Path on
CodeCademy.
"""

__all__ = ["rainwater"]


def main():
    test_array = [4, 2, 1, 3, 0, 1, 2]
    print(rainwater(test_array))  # 6


def rainwater(heights):
    """Return the rainwater captured by the array 'heights'."""
    # This function returns the amount of rainwater that would be 
    # captured by a histogram whose bars have heights given by the 
    # array "heights". 
    # 
    # This function calculates this value by using two pointers, one 
    # at the left end and one at the right end, and sets the left-bound and 
    # right-bound values to the values at each end. 
    # 
    # If the value at the left pointer is less than or equal to the 
    # value at the right pointer, the left-bound value is updated 
    # with the larger of the current left-bound value and the value 
    # at the left pointer. The total water is then updated with the 
    # difference between the left-bound value and the value at the 
    # left pointer (which will be zero if the left bound was just 
    # updated), and the left pointer is moved one unit to the right.
    # 
    # Otherwise, the right-bound value is updated with the larger of 
    # current right-bound value and the value at the right pointer.
    # The total water is then updated with the difference between the 
    # right-bound value and the value at the right pointer (which, 
    # again, will be zero if the right-bound value was just updated), 
    # and the right pointer is moved to the left by one unit.
    # 
    # This will continue until the pointers are equal. By this point, 
    # the calculation is complete, and the total water is returned by 
    # the function.
    
    total_water = 0
    left_pointer = 0
    right_pointer = len(heights) - 1
    left_bound = 0
    right_bound = 0

    while left_pointer < right_pointer:
        if heights[left_pointer] <= heights[right_pointer]:
            left_bound = max(left_bound, heights[left_pointer])
            total_water += left_bound - heights[left_pointer]
            left_pointer += 1
        else:
            right_bound = max(right_bound, heights[right_pointer])
            total_water += right_bound - heights[right_pointer]
            right_pointer -= 1

    return total_water


def _rainwater_naive(heights):
    """
    Return the rainwater captured by the array 'heights'.
    
    Uses a naive algorithm to calculate. Documented here for educational purposes only. Use the function 'rainwater' instead.
    """
    total_water = 0

    for i in range(1, len(heights) - 1):
        left_bound = 0
        right_bound = 0

        # We only want to look at the elements to the left of i,
        # which are the elements at the lower indices.
        for j in range(i+1):
            left_bound = max(left_bound, heights[j])

        # Likewise, we only want the elements to the right of i,
        # which are the elements at the higher indices.
        for j in range(i, len(heights)):
            right_bound = max(right_bound, heights[j])

        total_water += min(left_bound, right_bound) - heights[i]

    return total_water


if __name__ == "__main__":
    main()
