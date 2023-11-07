#!/usr/bin/python3
"""
    module that creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """
    Read a JSON file and return the corresponding Python object.

    Args:
        filename (str): The name of the JSON file to be loaded.

    Returns:
        object: The Python object representing the JSON data.

    """
    with open(filename) as jsonFile:
        return json.load(jsonFile)
