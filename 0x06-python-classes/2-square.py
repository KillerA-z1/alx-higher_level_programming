#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """ Definition of a Class Square """
    def __init__(self, size=0):
        """
        Initialize a Square object with a given size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
