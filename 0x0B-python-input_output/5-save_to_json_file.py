#!/usr/bin/python3
"""
    module that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write a JSON object to a file and return the filename.

    Args:
        my_obj (object): The Python object to be saved as JSON.
        filename (str): The name of the file to be created.

    Returns:
        str: The filename of the created JSON file.

    """
    with open(filename, "w", encoding="utf-8") as jsonFile:
        json.dump(my_obj, jsonFile)
    return filename
