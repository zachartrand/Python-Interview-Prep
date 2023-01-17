#!/usr/bin/env python3
"""
Prime Number Finder

Create a prime_finder() function that takes in a number, n, and returns
all the prime numbers from 1 to n (inclusive). As a reminder, a prime
number is a number that is only divisible by 1 and itself.

For example, prime_finder(11) should return [2, 3, 5, 7, 11].

Variations of this challenge have been reported to have been asked at
interviews with Facebook. If you’ve covered the material in Pass the
Technical Interview with Python or an equivalent, you should be able to
solve this challenge. If you have trouble, try refreshing your
knowledge there first.

From the Prime Number Finder Challenge at CodeCademy.
"""

from typing import List


def prime_finder(n: int) -> List[int]:
    if n < 2:
        return []
    elif n == 2:
        return [2]
    elif n < 5:
        return [2, 3]

    # For n above 4, use a sieve of Eratosthenes.
    RANGE_MAX: int = n + 1
    prime_sieve: List[bool] = [True for _ in range(RANGE_MAX)]

    # 0 and 1 are not prime.
    prime_sieve[0] = False
    prime_sieve[1] = False

    # Set all multiples of 2 to False.
    for i in range(4, RANGE_MAX, 2):
        prime_sieve[i] = False

    # Loop through all odd numbers up to the square root of RANGE_MAX.
    # If the number is prime, set all of its odd multiples to False.
    for i in range(3, int(RANGE_MAX**0.5) + 1, 2):
        if prime_sieve[i]:
            for j in range(i*i, RANGE_MAX, i*2):
                if prime_sieve[j]:
                    prime_sieve[j] = False

    # Return the primes using list comprehension.
    # This is more efficient than appending to a list.
    return [prime for prime, is_prime in enumerate(prime_sieve) if is_prime]


if __name__ == "__main__":
    print("List of primes up to 11:")
    print(prime_finder(11))  # [2, 3, 5, 7, 11]
