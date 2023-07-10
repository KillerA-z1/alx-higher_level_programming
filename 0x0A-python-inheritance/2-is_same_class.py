#!/usr/bin/python3
"""
Function is_same_class
"""


def is_same_class(obj, a_class):
    """Check if an object is of the exact class specified.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
    True if the object is an instance of the specified class, False otherwise.
    """
    return obj.__class__ is a_class
