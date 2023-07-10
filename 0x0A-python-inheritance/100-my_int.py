#!/usr/bin/python3
"""
Module: MyInt
"""


class MyInt(int):
    """
    MyInt class that inherits from int.
    """

    def __eq__(self, other):
        """
        Compare equality between MyInt objects.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the objects are instances of MyInt, False otherwise.
        """
        return isinstance(other, MyInt)

    def __ne__(self, other):
        """
        Compare inequality between MyInt objects.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the objects are not instances of MyInt,
                False otherwise.
        """
        return not isinstance(other, MyInt)
