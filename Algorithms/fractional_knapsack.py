#!/usr/bin/env python3
"""
Fractional Knapsack

Implementation of the fractional knapsack problem in Python
"""

from typing import Sequence


def main():
    weight_cap = 50
    values = [120, 60, 100]
    weights = [30, 10, 20]
    print(f"Item values: {values}")
    print(f"Item weights: {weights}")
    print(f"Knapsack weight cap: {weight_cap}")
    print()
    
    max_value = fractional_knapsack(weight_cap, weights, values)
    print(f"Max value: {max_value}.")


def fractional_knapsack(
        weight_cap: float, 
        weights: Sequence[float], 
        values: Sequence[float]
        ) -> float:
    """
    Return the highest value that can be placed in a knapsack with a 
    weight limit of 'weight_cap' given lists of item values and weights.

    The Fractional Knapsack problem assumes that you can take part of 
    an item and add a fraction of an item's value to the knapsack.
    """
    weight_value = [(weight, value) for weight, value in zip(weights, values)]
    weight_value.sort(key=lambda x: x[1]/x[0], reverse=True)

    final_value = 0.0
    for weight, value in weight_value:
        if weight <= weight_cap:
            weight_cap -= weight
            final_value += value
        
        else:
            final_value += value*weight_cap / weight
            break

    return final_value


if __name__ == "__main__":
    main()
