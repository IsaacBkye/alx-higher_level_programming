#!/usr/bin/python3


""" Module for class parent-child comparison"""


def is_kind_of_class(obj, a_class):
    """
    If the object is an instance of a_class, True
    if the object is an instance of a class that inherited from a_class, True
    otherwise False.
    """
    return (isinstance(obj, a_class))
