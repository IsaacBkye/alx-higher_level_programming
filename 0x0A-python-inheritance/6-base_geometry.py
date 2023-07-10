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
