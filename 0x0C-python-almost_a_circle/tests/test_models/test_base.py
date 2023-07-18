#!/usr/bin/python3
import unittest
import sys
import pep8
from io import StringIO
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


""" This is the containment for all unittest base cases"""


class testBase(unittest.TestCase):
    """
    Class to contain functions to run multiple tests
    """
    def set_up(self):
        """
        Method to redirect stdout to check
        outpute of functions relying on print
        """
        sys.stdout = StringIO()

    def tear_down(self):
        """
        Function to clean everything up after running
        setup
        """
        sys.stdout = sys.__stdout__

    def t_pep8_m(self):
        """
        Testing for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def t_pep8_t(self):
        """
        Testing for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def t_documentation(self):
        """
        Test if documentation is created and correct
        """
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(Base.create.__doc__)
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(Base.from_json_string.__doc__)
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(Base.save_to_file.__doc__)
        self.assertTrue(hasattr(Base, "load_from_file"))
        self.assertTrue(Base.load_from_file.__doc__)

    def t_id_1(self):
        """
        Check for id method
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def t_id_2(self):
        """
        After run ids
        """
        Base._Base__nb_objects = 0
        bas = Base()
        self.assertEqual(bas.id, 1)

    def t_id_3(self):
        """
        When random arguments are passed to check
        """
        Base._Base__nb_objects = 0
        t1 = Base(22)
        self.assertEqual(t1.id, 22)
        t2 = Base(-33)
        self.assertEqual(t2.id, -33)
        t3 = Base()
        self.assertEqual(t3.id, 1)

    def t_set_nb(self):
        """
        To set nb_objects as private
        """
        b = Base(33)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def t_dict(self):
        """To check if dictionary
        is working
        """
        r1 = Rectangle(11, 8, 3, 9, 2)
        d1 = r1.to_dictionary()
        j = {'x': 3, 'id': 2, 'y': 9, 'height': 8, 'width': 11}
        jd = Base.to_json_string([d1])
        self.assertEqual(d1, j)
        self.assertEqual(type(d1), dict)
        self.assertEqual(type(jd), str)

    def t_from_json_string(self):
        """
        To check from json to string
        conversion
        """
        s = '[{"id": 10, "width": 11, "height": 12, "x": 13, "y": 14}, \
{"id": 11, "width": 13, "height": 15, "x": 17, "y": 19}]'
        js = Base.from_json_string(s)
        self.assertTrue(type(js) is list)
        self.assertEqual(len(js), 2)

    def t_from_json_string_empty(self):
        """
        To check if it works with
        empty string or none
        """
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

    def t_rect(self):
        """
        To check for rectangle creation
        """
        R1 = Rectangle(3, 4, 5)
        R1_dict = R1.to_dictionary()
        R2 = Rectangle.create(**R1_dict)
        self.assertNotEqual(R1, R2)

    def t_sq(self):
        """
        To check for square creation
        """
        S1 = Square(40, 50, 60, 70)
        S1_dict = S1.to_dictionary()
        S2 = Rectangle.create(**S1_dict)
        self.assertNotEqual(S1, S2)

    def t_file_rect(self):
        """
        To check if file loads from rect
        """
        R1 = Rectangle(30, 30, 30, 20)
        R2 = Rectangle(201, 1)
        lR = [R1, R2]
        Rectangle.save_to_file(lR)
        lR2 = Rectangle.load_from_file()
        self.assertNotEqual(lR, lR2)

    def t_file_square(self):
        """
        To check if file loads from square
        """
        S1 = Square(20)
        S2 = Square(40, 40, 50, 60)
        lS = [S1, S2]
        Square.save_to_file(lS)
        lS2 = Square.load_from_file()
        self.assertNotEqual(lS, lS2)
