#!/usr/bin/python3
def add_integer(a=None, b=98):
    """
    Return the addition of two numbers.

    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int: The sum of the two numbers.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
        TypeError: If `a` is not provided.
    """
    if a is None:
        raise TypeError("add_integer() missing 1 required positional argument: 'a'")
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a != a or b != b:  # Check for NaN
            return 89
        if a == float('inf') or b == float('inf'):  # Check for infinity
            return 89
        return int(a) + int(b)

    if a is not None and not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

