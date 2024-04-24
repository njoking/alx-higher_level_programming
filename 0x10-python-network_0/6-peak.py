#!/usr/bin/python3
"""
Module that contains the function find_peak
"""


def find_peak(list_of_integers):
    """
    Finds a peak element in a list of unsorted integers.
    A peak element is an element that is greater than or equal to its neighbors.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: A peak element from the list, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
