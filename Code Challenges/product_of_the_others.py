#!/usr/bin/env python3
"""
Product of Everything Else

Create a product_of_the_others() function that takes in an array of
integers and replaces each number in the array with the product of all
the numbers in the array except the number at that index itself.

For example, product_of_the_others([1, 2, 3, 4, 5]) should return
[120, 60, 40, 30, 24], and product_of_the_others([5, 5, 5]) should
return [25, 25, 25].
"""


def product_of_the_others(array):
    # This function creates the result array by looping through the
    # array twice.
    #
    # On the first loop, two things are recorded: the number of zeroes
    # encountered in the array and the product of all the nonzero
    # numbers in the array.
    #
    # If the number of zeroes is two or more, then the product of all
    # numbers except the number at a given location will always be zero,
    # so the program returns an array of zeroes if the count of zeroes
    # exceeds one (1).
    #
    # If there is only one zero, then the product is zero everywhere
    # except at the index that contains zero, which equals the product
    # of all the other, nonzero numbers.
    #
    # Otherwise, the resulting array will contain the total product of
    # all of the numbers in the array divided by the number at the
    # given index.
    #
    # This function runs in O(n) time, as it loops through the array
    # twice: once to get the product and number of zeroes, twice to
    # find the values of the new array and assign them. The auxilliary
    # memory used in this function is O(n), since it creates a new
    # array to return the final values. This function can be made to
    # change the array in-place, which would make it use O(1)
    # auxilliary memory.

    # If there are fewer than two numbers in the array, there are no
    # numbers to multiply, so return the original array.
    if len(array) < 2:
        return array

    # First loop to get zeroes and product.
    zeroes = 0
    product = 1
    for number in array:
        if number == 0:
            zeroes += 1
            if zeroes > 1:
                return [0 for number in array]
        else:
            product *= number

    # Second loop to calculate and assign values to the result array.
    products = [None for number in array]
    for i, number in enumerate(array):
        if number == 0:
            products[i] = product
        elif zeroes == 1:
            products[i] = 0
        else:
            products[i] = product // number

    return products


if __name__ == "__main__":
    print(product_of_the_others([1, 2, 3, 4, 5]))  # [120, 60, 40, 30, 24]
