"""
The knapsack problem.
"""

__all__ = ["knapsack"]


def main():
    weight_cap = 50
    weights = [31, 10, 20, 19, 4, 3, 6]
    values = [70, 20, 39, 37, 7, 5, 10]
    print(knapsack(weight_cap, weights, values))  # 107


def knapsack(weight_cap, weights, values, threshold=20):
    """
    Return the maximum value of items that can fit in a knapsack 
    for a given set of weight_cap, weights, and values.
    """
    size = len(weights)
    if size <= threshold:
        return _recursive_knapsack(weight_cap, weights, values, size)
    
    return _dynamic_knapsack(weight_cap, weights, values)


def _recursive_knapsack(weight_cap, weights, values, i):
    """
    Return the maximum value of items that can fit in a knapsack 
    for a given set of weight_cap, weights, and values.

    Recursive algorithm for the Knapsack Problem. Runs in O(2^n) time.
    Should be used for a low number of items. For a large number of 
    items, use dynamic_knapsack instead.
    """
    if weight_cap == 0 or i == 0:
        return 0
    elif weights[i - 1] > weight_cap:
        return _recursive_knapsack(weight_cap, weights, values, i - 1)
    else:
        include_item = values[i - 1] + _recursive_knapsack(
            weight_cap - weights[i - 1], weights, values, i - 1)

        exclude_item = _recursive_knapsack(
            weight_cap, weights, values, i - 1)

        return max(include_item, exclude_item)


def _dynamic_knapsack(weight_cap, weights, values):
    """
    Return the maximum value of items that can fit in a knapsack 
    for a given set of weight_cap, weights, and values.

    Dynamic implementation of the Knapsack Problem. 
    
    Runs in O(weight_cap*number_of_items) time, where 
    number_of_items == len(weights). Good for large lists of items.
    """
    # In this implementation of the Knapsack Problem, a matrix is set 
    # up with a number of rows equal to the number of items plus one 
    # and a number of columns equal to the weight cap plus one.
    # This means that that calling the row of the matrix with 
    # matrix[i] returns all the values where there are up to 'i' items 
    # in the knapsack. Calling the column with matrix[i][j] gets you 
    # the maximum value you can carry in the knapsack where the 
    # knapsack has up to 'i' items with a weight cap of 'j'.
    # 
    # Once every value for every possible combination of items and 
    # weight_cap is calculated and stored, the bottom-right value of 
    # the matrix will contain the max value.

    rows = len(weights) + 1
    cols = weight_cap + 1

    # Set up 2D array
    matrix = [[] for _ in range(rows)]
    # Set all elements of row 0 to 0.
    matrix[0] = [0 for _ in range(cols)]

    # Iterate through every row other than row 0.
    for index in range(1, rows):
        # Initialize columns for this row.
        matrix[index] = [-1 for _ in range(cols)]
        matrix[index][0] = 0
        item_index = index - 1

        # Iterate through every column other than column 0.
        for weight in range(1, cols):
            if weights[item_index] <= weight:
                include_item = (
                    matrix[item_index][weight - weights[item_index]]
                    + values[item_index]
                )
                exclude_item = matrix[item_index][weight]
                matrix[index][weight] = max(include_item, exclude_item)

            else:
                matrix[index][weight] = matrix[index-1][weight]

    # Return the bottom-right value of the matrix.
    return matrix[rows-1][weight_cap]


if __name__ == "__main__":
    main()
