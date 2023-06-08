#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = 1
    arg = sys.argv
    if len(arg) == 1:
        print("{} arguments.".format(len(arg) - 1))
    if len(arg) == 2:
        print("{} argument:".format(len(arg) - 1))
        print("{}: {}".format(j, arg[j]))
    if len(arg) > 2:
        print("{} arguments:".format(len(arg) - 1))
        for i in range(len(arg)-1):
            print("{}: {}".format(j, arg[j]))
            j += 1
