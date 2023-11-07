#!/usr/bin/python3
"""
module that write and return the length of file
"""


def write_file(filename="", text=""):
    """
    Write the given text to a file specified by the filename and
    return the length of the written text.

    Args:
        filename (str): The name of the file to write. If not specified,
                        an empty string is used.
        text (str): The text to write to the file. If not specified,
                    an empty string is used.

    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
