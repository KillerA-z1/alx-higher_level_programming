#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return

    for num in range(len(my_list), 0, -1):
        print("{:d}".format(my_list[num - 1]))
