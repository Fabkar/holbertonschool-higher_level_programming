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
        self.size = size

    @property
    def size(self):
        """ Getter to size"""
        return self.__size

    @size.setter
    def size(self, size):
        """ Setter to size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return the area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print # making a square"""
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
