#!/usr/bin/python3
"""
Module: AttributeAdder
"""


def add_attribute(obj, attr, value):
    """
    Add an attribute to the object.

    Args:
        obj: The object to add the attribute to.
        attr: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object does not support adding attributes.

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        obj.__setattr__(attr, value)
