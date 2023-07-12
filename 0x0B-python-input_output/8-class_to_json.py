#!/usr/bin/python3


"""Module for exporting class to JSON"""


def class_to_json(obj):
    """
    Returns dictionary description with simple data structure
    """
    return vars(obj)
