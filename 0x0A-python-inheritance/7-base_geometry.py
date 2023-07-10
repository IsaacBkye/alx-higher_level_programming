#!/usr/bin/python3


""" Module for basic geometry"""


class BaseGeometry():
    """
    BaseGeometry class for basic calc.
    """

    def area(self):
        """
        Excpetion for when area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Values are validatedif value is not 
        an integer: raise a TypeError exception.
        Or if value is less or equal to 0: raise a ValueError
        """
        if (type(value) != int):
            raise TypeError(name + " must be an integer")
        if (value <= 0):
            raise ValueError(name + " must be greater than 0")
