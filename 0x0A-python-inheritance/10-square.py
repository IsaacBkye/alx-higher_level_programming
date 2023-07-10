#!/usr/bin/python3


"""Module for Basic rectangle calc"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class inherited from Rectangle.
    """

    def __init__(self, size):
        """
        Constructor/initializer method
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
