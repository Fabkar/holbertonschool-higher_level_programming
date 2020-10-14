#!/usr/bin/python3
"""
Unitest for model/base.py
"""
import unittest
import inspect
from models.base import Base, __doc__ as mrdoc
from models.rectangle import Rectangle, __doc__
from models.square import Square, __doc__


class TestBase(unittest.TestCase):
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


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""
    def test_to_json_string_noArg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_moreArg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_to_json_string_rectangle_type(self):
        self.assertEqual(str, type(Base.to_json_string(
            [Rectangle(1, 2, 3, 4, 5).to_dictionary()])))

    def test_to_json_string_rectangle_aDict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_twoDicts(self):
        list_dicts = [Rectangle(2, 3, 5, 19, 2).to_dictionary(), Rectangle(
            4, 2, 4, 1, 12).to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_Type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_Dict(self):
        self.assertTrue(len(
            Base.to_json_string([Square(10, 2, 3, 4).to_dictionary()])) == 39)

    def test_to_json_string_square_Dicts(self):
        list_dicts = [Square(2, 10, 4, 3).to_dictionary(), Square(
            4, 5, 2, 21).to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empList(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

if __name__ == '__main__':
    unittest.main()
