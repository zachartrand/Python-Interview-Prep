#!/usr/bin/env python3
"""
Number Permutation

Create a program called makeNumber(z) which, when given an input of a
number (z), returns the number of all possible permutations of up to 5
digits (1 through 9 inclusive) that when added will equal z.

For example, if z is 3, your program will find that four permutations
of digits add up to that value (3, 2+1, 1+1+1, and 1+2), and thus
return 4.

You can limit makeNumber(z) to the use of five digits, meaning anything
input above 45 (9 + 9 + 9 + 9 + 9) will return no permutations.

Repeat use of a digit is acceptable: e.g. 1+1+1 would be a valid
addition of digits equalling 3.

Use of a single digit is acceptable as a permutation: e.g. 3 is itself
a valid permutation of digits that add up to 3.

makeNumber(z) is looking for permutations, not combinations: 1+5 and
5+1 would count as two unique possible ways to add to 6, not one.

If no permutations of the digits 1 through 9 add up to the number z,
your function should return 0. Here are more sample inputs and outputs:

    Input: z = 1
    Output: 1
    The permutations:
    1

    Input: z = 2
    Output: 2
    The permutations:
    1 + 1
    2

    Input: z = 4
    Output: 8
    The permutations:
    1 + 1 + 1 + 1
    1 + 1 + 2
    1 + 2 + 1
    1 + 3
    2 + 1 + 1
    2 + 2
    3 + 1
    4

The number of permutations can be quite high.

    Input: z = 6
    Output: 31

    Input: z = 12
    Output: 554

    Input: z = 21
    Output: 3703

    Input: z = 35
    Output: 980

    Input: z = 45
    Output: 1

This challenge was reported to have been asked in interviews at many
top companies, including Facebook. If you’ve covered the material in
Pass the Technical Interview with Python or an equivalent, you should
be able to solve this challenge. If you have trouble, try refreshing
your knowledge with the lesson on recursion.
"""

__all__ = ["perm", "makeNumber"]

solutions = [-1 for i in range(46)]
solutions[0] = 0
for i in range(1, 6):
    solutions[i] = 2**(i-1)


def perm(z: int, n: int) -> int:
    """
    Return the number of unique permutations of up to 'n' number of
    single-digit numbers (1 through 9) that sum up to 'z'.
    """
    if z == 0:
        return 1
    elif n == 0:
        return 0

    total: int = 0
    for i in range(1, 10):
        if z >= i:
            total += perm(z-i, n-1)
        else:
            break

    return total


def makeNumber(z: int) -> int:
    """
    Return the number of permutations of up to five (5) single-digit
    numbers that sum up to 'z'.
    """
    # Write your code here
    if z > 45 or z < 0:
        return 0

    n: int = solutions[z]
    if n < 0:
        n = perm(z, 5)
        solutions[z] = n

    return n


if __name__ == '__main__':
    for i in range(46):
        print(f"{i}: {makeNumber(i)}")
