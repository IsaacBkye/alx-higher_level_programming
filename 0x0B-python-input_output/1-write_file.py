#!/usr/bin/python3


"""Module to write text to file"""


def write_file(filename="", text=""):
    """Function to write text to file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
