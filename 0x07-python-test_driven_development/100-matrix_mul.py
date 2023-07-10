#!/usr/bin/python3
"""
Matrix Multiplication

This module provides a function for multiplying two matrices.

"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list): The first matrix represented as,
                    a list of lists of integers or floats.
        m_b (list): The second matrix represented as,
                    a list of lists of integers or floats.

    Returns:
        list: The resulting matrix after multiplying m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list,
                or if m_a or m_b is not a list of lists,
                or if any element in m_a
                or m_b is not an integer or float.
        ValueError: If m_a or m_b is empty ([] or [[]]),
                or if m_a and m_b cannot be multiplied,
                        due to incompatible dimensions.

    Examples:
        >>> matrix_mul([[2, 5], [3, 1]], [[4, 2], [6, 3]])
        [[32, 16], [18, 9]]
        # Multiply two matrices: [[2, 5], [3, 1]] and [[4, 2], [6, 3]]
        # The expected result is [[32, 16], [18, 9]]

        >>> matrix_mul([[5, 8]], [[2.0, 1], [3, 7.0]])
        [[16.0, 39.0]]
        # Multiply two matrices: [[5, 8]] and [[2.0, 1], [3, 7.0]]
        # The expected result is [[16.0, 39.0]]

        >>> matrix_mul([[-1, 3], [2, -4]], [[5, -2], [7, 1]])
        [[19, -5], [-6, -10]]
        # Multiply two matrices: [[-1, 3], [2, -4]] and [[5, -2], [7, 1]]
        # The expected result is [[19, -5], [-6, -10]]

    """

    # Validate m_a and m_b
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for sublist in m_a:
        if not isinstance(sublist, list):
            raise TypeError("m_a must be a list of lists")
    for sublist in m_b:
        if not isinstance(sublist, list):
            raise TypeError("m_b must be a list of lists")

    if not m_a or not all(m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not all(m_b):
        raise ValueError("m_b can't be empty")

    for sublist in m_a:
        for element in sublist:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for sublist in m_b:
        for element in sublist:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    a_cols = 0
    for element in m_a[0]:
        a_cols += 1
    b_rows = 0
    for row in m_b:
        b_rows += 1

    if a_cols != b_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    i = 0
    while i < len(m_a):
        j = 0
        while j < len(m_b[0]):
            k = 0
            while k < len(m_b):
                result[i][j] += m_a[i][k] * m_b[k][j]
                k += 1
            j += 1
        i += 1

    return result
