#!/usr/bin/python3
"""
Append the given text to the end of a file specified by the filename and
return the number of characters written.
"""


def append_write(filename="", text=""):

    """

    Args:
        filename (str): The name of the file to append. If not specified,
                        an empty string is used.
        text (str): The text to append to the file. If not specified,
                        an empty string is used.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
