"""
Maximize Stock Trading Profit

Given the daily values of a stock, create a function called
max_profit_days() that, given a list of integers, will return the index
value of the two elements that represent the day on which one should
have bought a share and the day on which one should have sold a share
based on the max profit.

A list of integers will represent the stock price at the beginning or
“opening bell” of each day for a week. You are required to buy and sell
only once. You also must buy a stock before selling it.

For example, given the list [17, 11, 60, 25, 150, 75, 31, 120], you can
assume that index 0 represents day 0 and index 7 represents day 7. In
this case, purchasing on day 1 and selling on day 4 would yield the
most profit. If we were to call
max_profit_days([17, 11, 60, 25, 150, 75, 31, 120]), the function would
return (1, 4).

This challenge and variations of it were reported to have been asked at
interviews with Google. If you’ve covered the material in Pass the
Technical Interview with Python or an equivalent, you should be able to
solve this challenge. If you have trouble, try refreshing your
knowledge there first.
"""

__all__ = "max_profit_days"


def main():
    from random import randint

    stock_prices = [randint(10, 200) for _ in range(8)]

    print(f"This week's stock prices: \n{stock_prices}")
    print()

    buy, sell = max_profit_days(stock_prices)
    profit = stock_prices[sell] - stock_prices[buy]
    print(f"Buy on day {buy}, sell on day {sell}, make {profit} dollars.")


def max_profit_days(stock_prices):
    # Write your code here:
    best_buy = 0
    min_buy = stock_prices[0]
    min_buy_day = 0
    best_sell = 1
    best_profit = stock_prices[best_sell] - min_buy
    for day in range(1, len(stock_prices)):
        price = stock_prices[day]
        if price < min_buy:
            min_buy = price
            min_buy_day = day
        else:
            profit = price - min_buy
            if profit > best_profit:
                best_profit = profit
                best_sell = day
                best_buy = min_buy_day

    return best_buy, best_sell


if __name__ == '__main__':
    main()
