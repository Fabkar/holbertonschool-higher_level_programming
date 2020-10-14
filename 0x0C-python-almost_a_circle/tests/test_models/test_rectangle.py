#!/usr/bin/python3
"""
Unittest classes
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle, __doc__
from models.square import Square


class Test_Rectangle(unittest.TestCase):
    """
    docstring
    """
    def test_without_arg(self):
        """ test without arg """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rect(self):
        """ test rectangle """
        r = Rectangle(10, 15)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 15)

    def test_one_arg(self):
        """ test one arg """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_rectangle_base(self):
        """ test rectangle base """
        self.assertIsInstance(Rectangle(10, 20), Base)

    def test_none_id(self):
        """ test none id """
        self.assertEqual(Base(None).id, Base(None).id - 1)

    def test_docstring(self):
        """ test doctring """
        self.assertTrue(len(Base.__doc__.strip()) > 0)
        self.assertTrue(len(Base.to_json_string.__doc__.strip()) > 0)
        self.assertTrue(len(Base.save_to_file.__doc__.strip()) > 0)
        self.assertTrue(len(Base.from_json_string.__doc__.strip()) > 0)
        self.assertTrue(len(Base.create.__doc__.strip()) > 0)
        self.assertTrue(len(Base.load_from_file.__doc__.strip()) > 0)
