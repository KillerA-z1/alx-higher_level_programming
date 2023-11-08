#!/usr/bin/python3
"""
Function inherits_from
"""


def inherits_from(obj, a_class):
    """Check if an object is a subclass of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is a subclass of the specified class,
        False otherwise.
    """
    return issubclass(type(obj), a_class) and obj.__class__ != a_class
