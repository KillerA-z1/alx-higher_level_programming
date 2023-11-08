#!/usr/bin/python3
"""
Function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class,
        or inherited from, the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class
        or inherited from it, False otherwise.
    """
    return isinstance(obj, a_class)
