#!/usr/bin/python3
def safe_print_list(my_list=[], limit=0):
    printed_count = 0
    index = 0

    while index < limit:
        try:
            print(f"{my_list[index]}", end="")
            printed_count += 1
        except IndexError:
            break
        index += 1

    print()
    return printed_count
