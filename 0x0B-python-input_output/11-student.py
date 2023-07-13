#!/usr/bin/python3


"""Module for Student class"""


class Student:
    """
    Student class definition
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializer/Constructor method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Dictionary of a Student instance with attrs validation
        """
        if (type(attrs) is list):
            newDict = {}
            Dict = vars(self)
            setDict = set(Dict)
            setList = set(attrs)
            keys = list(setDict & setList)
            for key in keys:
                newDict[key] = Dict[key]
            return (newDict)
        return vars(self)

    def reload_from_json(self, json):
        """
        To replace all attributes of the Student instance
        """
        for (key, value) in json.items():
            setattr(self, key, value)
