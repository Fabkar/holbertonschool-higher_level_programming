#!/usr/bin/python3
"""
Unitest for model/base.py
"""
import unittest
import pep8
import inspect
from models.base import Base, __doc__ as mrdoc


class TestBase(unittest. TestCase):
    """
    Test to Base Class
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

    def test_pep8(self):
        """check Test to pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0)

    def test_baseclass(self):
        """
        1. Base Class
        """
        b = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(Base._Base__nb_objects, 1)
        b2 = Base(3)
        self.assertEqual(b2.id, 3)
        self.assertEqual(Base._Base__nb_objects, 1)
        b2.id = 4
        self.assertEqual(b2.id, 4)
        b2.id = "Test"
        self.assertEqual(b2.id, "Test")


if __name__ == '__main__':
    unittest.main()
