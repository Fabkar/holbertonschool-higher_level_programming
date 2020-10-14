#!/usr/bin/python3
"""unittest square"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import inspect
import pep8


class test_square(unittest.TestCase):
    """unittest square"""
    def test_doctstring(self):
        """Test documentation"""
        self.assertTrue(len(Base.__doc__.strip()) > 0)
        self.assertTrue(len(Base.to_json_string.__doc__.strip()) > 0)
        self.assertTrue(len(Base.save_to_file.__doc__.strip()) > 0)
        self.assertTrue(len(Base.from_json_string.__doc__.strip()) > 0)
        self.assertTrue(len(Base.create.__doc__.strip()) > 0)
        self.assertTrue(len(Base.load_from_file.__doc__.strip()) > 0)

    def test_pep8(self):
        """Test PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/rectangle.py"])
        self.assertEqual(result.total_errors, 0)

    def test_square_success(self):
        """check success class work"""
        S = Square(1)
        self.assertEqual(S.size, 1)
        self.assertEqual(S.x, 0)
        self.assertEqual(S.y, 0)

    def test_instances(self):
        """check instances"""
        with self.assertRaises(TypeError):
            S = Square()
        with self.assertRaises(TypeError):
            S = Square(1, 2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
            S = Square(0)

if __name__ == "__main__":
    unittest.main()
