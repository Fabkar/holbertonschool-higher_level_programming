#!/usr/bin/python3
"""
Unitest for model/base.py
"""
import unittest
import inspect
from models.base import Base
from models.square import Square, __doc__ as mrdoc


class TestSquare(unittest. TestCase):
    """
    Test to Square Class
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

    def test_square_correct(self):
        """Checking each attribute of square"""
        r = Square(2)
        self.assertEqual(r.size, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)
