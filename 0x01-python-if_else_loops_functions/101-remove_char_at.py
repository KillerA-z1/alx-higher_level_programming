#!/usr/bin/python3
def remove_char_at(string, n):
    if n >= 0 and n < len(string):
        string = string[:n] + string[n+1:]
    return string
