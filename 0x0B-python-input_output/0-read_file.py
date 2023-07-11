#!/usr/bin/python3
def read_file(filename=""):
    """
    Read the contents of a text file (UTF8) and print it to stdout.

    Args:
        filename (str): The name of the file to read. If not specified,
                        an empty string is used.

    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
