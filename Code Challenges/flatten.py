#!/usr/bin/env python3
"""
Code Challenge for flattening an array from CodeCademy.
Text from problem below.


Flatten an Array
Write a function, flatten_array(), that takes in a 2-dimensional array,
flattens it into a 1-dimensional array, and returns it. You can assume
that you will only be given one or two-dimensional arrays

For example, flatten_array([1, 2, [3, 4, 5], 6, [7, 8], 9]) should
return [1, 2, 3, 4, 5, 6, 7, 8, 9].

This challenge was reported to have been asked at interviews with
Facebook, as well as right here at Codecademy! If you’ve covered the
material in Pass the Technical Interview with Python or an equivalent,
you should be able to solve this challenge. If you have trouble, try
refreshing your knowledge there first.
"""


def main():
    a = [1, 2, [3, 4, 5], 6, [7, 8], 9]
    print("Before:", a)
    print("After:", flatten_array(a))


def flatten_array(arr):
    # Write your code here
    flat = []
    for item in arr:
        if isinstance(item, type(arr)):
            flat.extend(flatten_array(item))
        else:
            flat.append(item)

    return flat


if __name__ == "__main__":
    main()
