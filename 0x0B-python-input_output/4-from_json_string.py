#!/usr/bin/python3
"""
    module that returns an object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Return a Python object from a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python object represented by the JSON string.

    """
    return json.loads(my_str)
