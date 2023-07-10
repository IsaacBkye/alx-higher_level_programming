#!/usr/bin/python3


""" Module for Lists"""


class MyList(list):
    """
    Class that inherits from list
    """
    def print_sorted(self):
        print(sorted(self))
