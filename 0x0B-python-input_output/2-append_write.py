#!/usr/bin/python3


"""Module for appending to a file"""


def append_write(filename="", text=""):
    """
    Writes a string to a text file, also returns the number of characters written
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
