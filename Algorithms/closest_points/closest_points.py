#!/usr/bin/env python3
"""
Closest Pair of Points

We are given an array of n points in the plane, and the problem is to
find out the closest pair of points in the array. This problem arises
in a number of applications. For example, in air-traffic control, you
may want to monitor planes that come too close together, since this may
indicate a possible collision.

Modified from C++ code from this GeeksForGeeks webpage:

    https://www.geeksforgeeks.org/closest-pair-of-points-onlogn-implementation
"""

__all__ = ["closest_distance", "get_distance"]

from math import hypot as _hypot, inf as _inf

THRESHOLD: int = 32  # Should be no lower than 3, no greater than 64.

# The first version of this module used a Point class to represent points. 
# I rewrote the module to apply to tuples or arrays representing points 
# instead, as that seemed more generally applicable.
# 
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def distance(self, other_point):
#         dx = self.x - other_point.x
#         dy = self.y - other_point.y

#         return _hypot(dx, dy)

#     def __str__(self):
#         return f"{self.x, self.y}"

#     def __repr__(self):
#         return f"{self.__class__.__qualname__}{(self.x, self.y)}"


def main():
    from random import randint

    size = 1000

    points = [(i+1, randint(1, 10*size)) for i in range(size)]

    # print("Points:")  # Uncomment these lines when 
    # print(points)     # 'size' is reasonably small.

    d, p1, p2 = closest_distance(points)

    print(f"The closest points are {p1} and {p2}, which are {d:.5f} units apart.")
    print()


def get_distance(point_1: tuple, point_2: tuple):
    """
    Return the distance between two points.
    """
    dx = point_1[0] - point_2[0]
    dy = point_1[1] - point_2[1]

    return _hypot(dx, dy)


def _closest_distance_naive(point_array):
    """
    Return the shortest distance between two points from an array of
    points.

    This function loops through the entire array, comparing the
    distance between all combinations of points.

    Time Complexity: O(n^2)
    """
    min_distance = _inf
    point_1 = ()
    point_2 = ()

    n = len(point_array)
    if n > 1:
        for i in range(n-1):
            point_i = point_array[i]
            for j in range(i+1, n):
                point_j = point_array[j]
                distance = get_distance(point_i, point_j)
                if distance < min_distance:
                    min_distance = distance
                    point_1 = point_i
                    point_2 = point_j

    return min_distance, point_1, point_2


def _closest_in_strip(strip):
    """
    Return the shortest distance between two points within a strip.
    """
    min_distance = _inf
    point_1 = ()
    point_2 = ()

    size = len(strip)
    if size < 8:
        return _closest_distance_naive(strip)

    for i in range(size-7):
        point_i = strip[i]
        for j in range(1, 8):
            point_i_plus_j = strip[i+j]
            distance = get_distance(point_i, point_i_plus_j)
            if distance < min_distance:
                min_distance = distance
                point_1 = point_i
                point_2 = point_i_plus_j

    return min_distance, point_1, point_2


def _closest_distance_recursive(point_array_x_sorted, point_array_y_sorted, left_index: int = 0):
    """
    Return the shortest distance between two points from an array of
    points using two sorted copies of the array, one by x-values and
    one by y-values.

    Parameters:
        point_array_x_sorted: The array of points sorted by x-value.

        point_array_y_sorted: The array of points sorted by y-value.

        left_index (int): The left-most index of point_array_x_sorted that 
            includes all the points in point_array_y_sorted. 
            Used for recursion. Default value is 0.
    
    Returns:
        min_distance (float): The closest distance between any two 
            points in the array.
        
        point_1: One of the two closest points.

        point_2: One of the two closest points.
    """
    size = len(point_array_y_sorted)

    # Use naive solution for small arrays.
    if size <= THRESHOLD:
        return _closest_distance_naive(point_array_y_sorted)

    # Find the point in the middle of the array 
    # to divide the problem into two subproblems.
    half_size = size // 2
    middle_index = half_size + left_index
    middle_point = point_array_x_sorted[middle_index]

    point_array_y_sorted_left = []
    point_array_y_sorted_right = []

    for i in range(size):
        point = point_array_y_sorted[i]
        if len(point_array_y_sorted_left) < half_size and (
            point[0] < middle_point[0]
            or (point[0] == middle_point[0]
                and point[1] < middle_point[1])):
            point_array_y_sorted_left.append(point)
        else:
            point_array_y_sorted_right.append(point)

    d_left, point_1_left, point_2_left = (
        _closest_distance_recursive(point_array_x_sorted, point_array_y_sorted_left, left_index))
    d_right, point_1_right, point_2_right = (
        _closest_distance_recursive(point_array_x_sorted, point_array_y_sorted_right, middle_index))

    if d_left <= d_right:
        min_distance = d_left
        point_1 = point_1_left
        point_2 = point_2_left
    else:
        min_distance = d_right
        point_1 = point_1_right
        point_2 = point_2_right

    y_sorted_strip = []
    for i in range(size):
        point = point_array_y_sorted[i]
        if abs(point[0] - middle_point[0]) < min_distance:
            y_sorted_strip.append(point)

    min_distance_strip, point_1_strip, point_2_strip = (_closest_in_strip(y_sorted_strip))

    if min_distance_strip < min_distance:
        return min_distance_strip, point_1_strip, point_2_strip

    return min_distance, point_1, point_2


def closest_distance(point_array):
    """
    Return the shortest distance between two points from an array of
    points.

    Parameters:
        point_array: an array of Point objects.

    Returns:
        float: Distance between the two closest points.
        Iterable[int or float]: The first of the two closest points.
        Iterable[int or float]: The second of the two closest points.

    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    size = len(point_array)

    # Skip sorting the points if the array is small.
    if size <= THRESHOLD:
        return _closest_distance_naive(point_array)

    point_array_x_sorted = sorted(point_array, key=lambda point: point)
    point_array_y_sorted = sorted(point_array_x_sorted, key=lambda point: point[1])

    return _closest_distance_recursive(point_array_x_sorted, point_array_y_sorted)


if __name__ == '__main__':
    main()
