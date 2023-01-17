#!/usr/bin/env python3
"""
Radix Sort

Implementation of Radix Sort in Python
"""

__all__ = ["radix_sort"]


def main():
    unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535,
                     959, 40, 641, 355, 689, 621, 183, 182, 524, 1]
    print("Unsorted:")
    print(unsorted_list)
    print()

    print("Sorting...")
    sorted_list = radix_sort(unsorted_list)
    print("Done!")
    print()

    print("Sorted:")
    print(sorted_list)


def radix_sort(to_be_sorted):
    maximum_value = max(to_be_sorted)
    max_exponent = len(str(maximum_value)) + 1
    being_sorted = to_be_sorted[:]

    for position in range(1, max_exponent):
        digits = [[] for _ in range(10)]

        for number in being_sorted:
            try:
                digit = int(str(number)[-position])
            except IndexError:
                digit = 0

            digits[digit].append(number)

        being_sorted = []
        for numeral in digits:
            being_sorted.extend(numeral)

    return being_sorted


if __name__ == "__main__":
    main()
