#!/usr/bin/python3
"""
Module defines a class Myint
"""


class MyInt(int):
    """
    class MyInt inherits from int
    """

    def __eq__(self, value):
        """
        it's true if self and other are Not equal
        """
        return int(self) != value

    def __ne__(self, value):
        """
        it's true if self and other are equal
        """
        return int(self) == value
