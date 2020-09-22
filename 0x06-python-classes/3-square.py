#!/usr/bin/python3
"""Class Square with a Private instance attribute init in 0"""


class Square:
    """print an attribute size"""
    def __init__(self, size=0):
        """
        Init of objects

        Args:
            size(int): size of square
            conditionals to evaluate type of variable
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
