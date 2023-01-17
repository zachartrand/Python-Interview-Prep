#!/usr/bin/env python3
"""
Stairmaster

Write a function, stairmaster(n), that will compute the number of ways
to climb a flight of n steps, taking 1, 2, or 3 steps at a time.

Take the example of climbing n = 4 steps. There are seven different
ways one can climb four stairs using 1, 2, or 3 steps at a time:
[1,1,1,1] [2,1,1] [1,2,1] [1,1,2] [2,2] [1,3] [3,1].

Make sure to find all permutations, not combinations, as the order
matters. Climbing one step then two steps is different from climbing
two steps then one step.

This challenge and variations of it were reported to have been asked at
interviews with Google. If you’ve covered the material in Pass the
Technical Interview with Python or an equivalent, you should be able to
solve this challenge. If you have trouble, try refreshing your
knowledge there first.
"""

__all__ = ["stairmaster_coin_sum", "stairmaster_fibo", "stairmaster_memoized"]

VALUES = {1: 1, 2: 2, 3: 4}


def main():
    print()
    print("Stairmaster solved using the coin sum function:")
    for i in range(-1, 11):
        print(i, stairmaster_coin_sum(i, [1, 2, 3]))
    print()

    print("Stairmaster solved using the memoized function:")
    print(4, stairmaster_memoized(4))
    print({k: VALUES[k] for k in sorted(VALUES.keys())})
    print()
    print("Memoized up to 20:")
    stairmaster_memoized(20)
    VALUES = {k: VALUES[k] for k in sorted(VALUES.keys())}

    [print(k, v) for k, v in VALUES.items()]
    print()

    print("Stairmaster solved using the Fibonacci function:")
    print(4, stairmaster_fibo(4))


def stairmaster_coin_sum(n, steps):
    if n < 1:
        return 0

    total = n + 1
    step_count = [0 for _ in range(total)]
    step_count[0] = 1

    for i in range(1, total):
        for step in steps:
            if i >= step:
                step_count[i] += step_count[i-step]

    return step_count[n]


def stairmaster_memoized(n):
    if n < 1:
        return 0

    answer = VALUES.get(n, None)
    if answer is not None:
        return answer

    steps = stairmaster_memoized(n-3) + stairmaster_memoized(n-2) + stairmaster_memoized(n-1)
    VALUES[n] = steps

    return steps


def stairmaster_fibo(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    a = 1
    b = 2
    c = 4
    for _ in range(n - 3):
        a, b, c = b, c, a + b + c

    return c


if __name__ == '__main__':
    main()
