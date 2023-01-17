#!/usr/bin/env python3
"""
Python Code Challenge from CodeCademy.

Change Please

You’re building an ATM and are tasked with determining how many
different ways you can “break” a given amount of money into different
bills.

Given an input amount of money input_money and a list of values coins
representing the possible denominations of coins the ATM can give back,
complete the function change_options(input_money, coins) so that it
returns the number of different ways the ATM could give you change.

For example, change_options(5, [1, 2, 5, 10, 100]) should return 4.
This is because there are 4 unique ways that the ATM can give change
for 5:

1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 2
1 + 2 + 2
5
You can assume input_money is positive and you can assume coins has at
least one value.

This challenge was reported to have been asked at interviews with
Google. If you’ve covered the material in Pass the Technical Interview
with Python or an equivalent, you should be able to solve this
challenge.
"""


def main():
    print(change_options(5, [1, 2, 5, 10, 100]))  # 4
    print()

    print("Number of ways to break a dollar:")
    print(change_options(100, [1, 5, 10, 25, 50]))  # 292
    print()

    print("Number of ways to break 20 dollars (bills only):")
    print(change_options(20, [1, 5, 10]))  # 9
    print()
    print("Number of ways to break 20 dollars "
          "(bills only, including the elusive 2 dollar bill):")
    print(change_options(20, [1, 2, 5, 10]))  # 40


def change_options(input_money, coins):
    coins = sorted(coins)
    range_max = input_money + 1
    options = [0 for _ in range(range_max)]
    options[0] = 1
    for coin_value in coins:
        for value in range(coin_value, range_max):
            options[value] += options[value - coin_value]

    return options[input_money]


if __name__ == "__main__":
    main()
