#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Finds and returns a peak element from a list of unsorted integers.

    A peak element is defined as an element that is greater than its neighbors.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: A peak element from the list, if one exists; otherwise, None.
    """
    if not list_of_integers:
        return None

    list_length = len(list_of_integers)
    if list_length == 1:
        return list_of_integers[0]
    elif list_length == 2:
        return max(list_of_integers)

    middle_index = list_length // 2
    middle_element = list_of_integers[middle_index]
    # Check if the middle element is a peak
    if middle_index > 0 and middle_index < list_length - 1:
        if middle_element > list_of_integers[middle_index - 1] and middle_element > list_of_integers[middle_index + 1]:
            return middle_element
        elif middle_element < list_of_integers[middle_index - 1]:
            return find_peak(list_of_integers[:middle_index])
        else:
            return find_peak(list_of_integers[middle_index + 1:])
    # Edge case: middle element is at the boundary
    else:
        if middle_index == 0:
            if middle_element > list_of_integers[middle_index + 1]:
                return middle_element
            else:
                return find_peak(list_of_integers[middle_index + 1:])
        elif middle_index == list_length - 1:
            if middle_element > list_of_integers[middle_index - 1]:
                return middle_element
            else:
                return find_peak(list_of_integers[:middle_index])
