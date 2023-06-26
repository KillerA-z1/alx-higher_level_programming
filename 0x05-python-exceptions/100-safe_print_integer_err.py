#!/usr/bin/python3
import sys


def safe_print_integer_err(number):
    try:
        print("{:d}".format(number))
        return True
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return False
