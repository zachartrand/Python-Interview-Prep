#!/usr/bin/env python3
"""
Linear Search module.
"""
def main():
    number_list = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
    target_number = 33
    print("Number list:")
    print(number_list)
    print(f"Target number: {target_number}")
    print()
    try:
        result = linear_search(number_list, target_number)
        print(f"{target_number} is found at these indices:")
        print(result)

    except ValueError as error_message:
        print(f"{error_message}\n")

    tour_locations = ["New York City", "Los Angeles", "Bangkok",
                      "Istanbul", "London", "New York City", "Toronto"]
    target_city = "New York City"
    print("Subway stops:")
    print(tour_locations)
    print(f"Target City: {target_city}")
    print(f"{target_city} is found at these indices:")
    tour_stops = linear_search_all_matches(tour_locations, target_city)
    print(tour_stops)


def linear_search(search_list, target_value):
    """
    Return the first item in a list that matches the target_value.

    This is a linear search algorithm.

    Parameters:
        search_list (iterable): A list of items to search through.

        target_value: The value to search for.

    Returns:
        index (int): The index of the matching item.
    """
    for index, item in enumerate(search_list):
        # print(item)
        if item == target_value:
            return index

    raise ValueError(f"{target_value} not in list")


def linear_search_all_matches(search_list, target_value):
    """
    Return all items in a list that match the target_value.

    This is a linear search algorithm.

    Parameters:
        search_list (iterable): A list of items to search through.

        target_value: The value to search for.

    Returns:
        matches (List(int)): List of indices of the matching items.
    """
    matches = []
    for index, item in enumerate(search_list):
        if item == target_value:
            matches.append(index)
    if not matches:
        raise ValueError(f"{target_value} not in list")

    return matches


if __name__ == "__main__":
    main()
