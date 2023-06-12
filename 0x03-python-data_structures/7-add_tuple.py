#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    row = tuple_a + (0, 0)
    column = tuple_b + (0, 0)
    result = (row[0] + column[0], row[1] + column[1])
    return result
