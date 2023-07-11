#!/usr/bin/python3
"""
    This Module reads a file
"""


def read_file(filename=""):
    """
    Read the contents of a text file (UTF8) and print it to stdout.

    Args:
        filename (str): The name of the file to read. If not specified,
                        an empty string is used.

    """
    with open(filename, encoding="utf-8") as file:
        contents = file.read()
        print(contents, end="")
        file.closed
