#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        c = add(c, sum(range(4, 6)))
        return c
    else:
        return sub(a, b)
