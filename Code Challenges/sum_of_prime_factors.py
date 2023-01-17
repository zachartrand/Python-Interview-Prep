#!/usr/bin/env python3
"""
Sum of Prime Factors
Create a sum_of_prime_factors() function that takes in an integer n and
returns the sum of all of its prime factors. As a reminder, a prime
number is a number whose only factors are one and itself. Therefore, a
prime factor is a factor of a given number that itself is a
prime number.

For example, sum_of_prime_factors(91) should return 20 since its prime
factors are 13 and 7.

This challenge and variations of it were reported to have been asked at
interviews with Google. If you’ve covered the material in Pass the
Technical Interview with Python or an equivalent, you should be able to
solve this challenge. If you have trouble, try refreshing your
knowledge there first.

Source: https://www.codecademy.com/code-challenges/code-challenge-sum-of-prime-factors-python
"""


def sum_of_prime_factors(n):
    """
    Return the sum of the unique prime factors of n.
    """
    # There are no prime numbers less than 2, so return 0 for these values.
    if n < 2:
        return 0

    # Create an array of length n+1. Each value in the array will be the
    # sum of prime factors of that value's index.
    array = [0 for _ in range(n+1)]
    for number in range(2, n+1):
        # If the value of array[number] is 0, that number must be prime.
        if array[number] == 0:
            array[number] = number

            for i in range(2, n//number + 1):
                array[i*number] = number + array[i]

            power = number*number
            while power <= n:
                array[power] = number
                for j in range(2, n//power + 1):
                    array[j*power] -= number
                power *= number

    return array[n]


if __name__ == '__main__':
    print(sum_of_prime_factors(91))
