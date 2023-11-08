#!/usr/bin/python3
"""
Sorted List

This module defines custom class `MyList` that extends built-in `list` class
and provides a method `print_sorted()` to print a sorted version of the list.

"""


class MyList(list):
    """
    Sorted List class.

    This class extends the built-in `list` class and provides additional
    functionality for sorting and printing the list.

    Attributes:
        list: The list of elements.

    Methods:
        __init__(): Initializes an empty list.
        print_sorted(): Prints the sorted list.



    """

    def __init__(self):
        """
        Initialize an empty list.

        """

        self.list = []

    def print_sorted(self):
        """
        Print the sorted list.

        """

        print(sorted(self))
