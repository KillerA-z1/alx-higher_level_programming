#!/usr/bin/python3
"""
Object Attribute and Method Lookup

This module provides
a function for listing all available attributes and methods of an object.

"""


def lookup(obj):
    """
    List attributes and methods of an object.

    Args:
        obj: An object.

    Returns:
        list: A list of attributes and methods of the object.

    """

    return dir(obj)
