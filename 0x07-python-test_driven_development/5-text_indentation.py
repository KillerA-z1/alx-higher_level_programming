#!/usr/bin/python3
"""
Function that prints a text with 2 new lines
after each of these characters: ., ? and :

Doctest check the tests
Always success
"""


def text_indentation(text):
    """Validate the input text"""
    if type(text) not in [str]:
        raise TypeError("text must be a string")

    flag = 0
    for i in text:
        if flag == 0:
            if i == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                flag = 0
            else:
                print(i, end="")
