#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python 1-square.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
class Square:
    """Square is an empty class.
    
    Args:
        None.

    Returns:
        None.

    """
    def __init__(self, size=0, position=(0, 0)):
        """Constructor function called

    The format for a parameter is::

        name: description
            The description may span multiple lines. Following
            lines should be indented. The "(type)" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Args:
        size: The first parameter.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.
        """
        self.position = position
        self.__size = size

    def area(self):
        """Constructor function called

    The format for a parameter is::

        name: description
            The description may span multiple lines. Following
            lines should be indented. The "(type)" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Args:
        size: The first parameter.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """This is the property
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """This is the setter
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Another function doc
        """
        if (self.size == 0):
            print()
        else:
            for i in range(0, self.position[1]):
                print()
            for i in range(0, self.size):
                print((" " * self.position[0]) + ("#" * self.size))

    @property
    def position(self):
        """ Statement about position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Statement about setter
        """
        if (type(value) != tuple) or (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) != int) or (type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
