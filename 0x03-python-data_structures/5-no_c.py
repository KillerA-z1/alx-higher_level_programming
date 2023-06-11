#!/usr/bin/python3
def no_c(my_string):
    empty_str = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            empty_str += char
    return empty_str
