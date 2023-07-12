#!/usr/bin/python3


"""Module for exporting JSON object"""


import json


def from_json_string(my_str):
    """
    JSON representation of an object (string)
    """
    return json.loads(my_str)
