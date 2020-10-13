#!/usr/bin/python3
"""
Unitest for model/base.py
"""

import pep8
import unittest
import inspect
from models.base import Base
from models.rectangle import Rectangle, __doc__ as mrdoc


class TestRectangle(unittest. TestCase):
    """
    Test to Rectangle Class
    """
    def test_docstring(self):
        """ check each base class with docstrings"""
        self.assertTrue(len(mrdoc.strip()) > 0)
        self.assertTrue(len(Base.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.ismethod)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.isfunction)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)

    def test_rectangle_correct(self):
        """Checking each attribute of Rectangle"""
        r = Rectangle(2, 3)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 3)

    def test_pep8(self):
        """check Test to pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/rectangle.py"])
        self.assertEqual(result.total_errors, 0)

    def test_validator(self):
        """checks the calling of Rectangle"""
        with self.assertRaises(TypeError):
            r = Rectangle(8)
        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(TypeError):
            r = Rectangle(5, 6, 2, 4, 9, 0)

    def test_negative_attributes(self):
        """checking Negative attribute"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-2, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(2, -1)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 0, 0)

    def test_attributes_float(self):
        """checking type float in attributes"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(8.5, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(8, 5.0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, 2.0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(5, 6, 4, 9.1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(9, float('inf'))

    def test_attributesstring(self):
        """checking type str in attributes"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("Base", 1)

    def test_area(self):
        """cheacking the area of rectangle"""
        r = Rectangle(2, 4)
        self.assertEqual(r.area(), 8)
        r2 = Rectangle(789965564, 534353453332)
        self.assertEqual(r2.area(), 422120827136761059248)
        with self.assertRaises(TypeError):
            r2.area(5)
