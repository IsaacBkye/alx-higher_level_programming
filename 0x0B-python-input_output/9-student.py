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

    def to_json(self):
        """
        Dictionary of a Student instance
        """
        return vars(self)
