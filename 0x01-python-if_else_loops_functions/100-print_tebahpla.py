#!/usr/bin/python3
for index in range(0, 26):
    print("{}".format(
        chr(ord('z') - index).upper()
        if index % 2 == 1
        else chr(ord('z') - index)
    ), end='')
