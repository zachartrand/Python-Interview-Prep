import random


def bubble_sort(arr, comparison_function):
    swaps = 0
    sorted = False
    while not sorted:
        sorted = True
        for idx in range(len(arr) - 1):
            if comparison_function(arr[idx], arr[idx + 1]):
                sorted = False
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaps += 1
    print(f"Bubble sort: There were {swaps} swaps")
    return arr


def quicksort(array, comparison_function, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start >= end:
        return
    pivot_idx = random.randrange(start, end + 1)
    pivot_element = array[pivot_idx]
    array[end], array[pivot_idx] = array[pivot_idx], array[end]
    less_than_pointer = start
    for i in range(start, end):
        if comparison_function(pivot_element, array[i]):
            array[i], array[less_than_pointer] = array[less_than_pointer], array[i]
            less_than_pointer += 1
    array[end], array[less_than_pointer] = array[less_than_pointer], array[end]
    quicksort(array, comparison_function, start, less_than_pointer - 1)
    quicksort(array, comparison_function, less_than_pointer + 1, end)
