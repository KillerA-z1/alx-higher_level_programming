#!/usr/bin/python3
def matrix_mul(m_a, m_b):
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
