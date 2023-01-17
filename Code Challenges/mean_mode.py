#!/usr/bin/env python3
"""
Calculate the Mean and Mode
Create a stats_finder() function that takes in a list of numbers and
returns a list containing the mean and mode, in that order. As a
reminder, the mean is the average of the values and the mode is the
most occurring value. If there are multiple modes, return the mode with
the lowest value. Make sure that you write your functions and find
these answers from scratch – don’t use imported tools!

For example, stats_finder([500, 400, 400, 375, 300, 350, 325, 300])
should return [368.75, 300].

Variations of this challenge were reported to have been asked at
interviews with Amazon. If you’ve covered the material in Pass the
Technical Interview with Python or an equivalent, you should be able
to solve this challenge. If you have trouble, try refreshing your
knowledge with its Algorithmic Complexity content.
"""

__all__ = "stats_finder"


def main():
    a = [500, 400, 400, 375, 300, 350, 325, 300]
    print("Array:", a)
    print("Mean and Mode:", stats_finder(a))


def stats_finder(array):
    counts = {}
    mean = 0
    for number in array:
        mean += number
        counts[number] = counts.get(number, 0) + 1

    mean /= len(array)

    mode = None
    for number in sorted(counts.keys()):
        if counts[number] > counts.get(mode, 0):
            mode = number

    return [mean, mode]


if __name__ == '__main__':
    main()
