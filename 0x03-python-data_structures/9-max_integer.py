#!/usr/bin/python3
def max_integer(my_list=[]):
    list_max = None if not my_list else my_list[0]
    for char in my_list:
        list_max = char if char > list_max else list_max
    return list_max
