#!/usr/bin/python3

"""
Return the dictionary description for the JSON serialization.
"""


def class_to_json(obj):
    """
    Return the dictionary description of given object for JSON serialization.

    Args:
        obj: An object to be serialized.

    Returns:
        dict: A dictionary representing the serialized object.

    """
    return obj.__dict__
