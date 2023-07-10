#!/usr/bin/python3


"""Module for class comparison """


def is_same_class(obj, a_class):
    """
    True if the object is a_class instance; otherwise False.
    """
    return (type(obj) is a_class)
