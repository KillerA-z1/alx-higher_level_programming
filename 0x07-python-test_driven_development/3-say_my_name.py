#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Print the name by combining first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.

    Returns:
        None
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the name
    full_name = f"My name is {first_name} {last_name}".strip()
    print(full_name)
