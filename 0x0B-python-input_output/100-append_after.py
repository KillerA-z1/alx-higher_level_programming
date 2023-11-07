#!/usr/bin/python3
"""
Append a string after a specific line in a text file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append a new string after a specific line in a text file.

    Args:
        filename (str): The name of the text file.
        search_string (str): The string to search for in the file.
        new_string (str): The string to append after the search string.

    Returns:
        None
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
