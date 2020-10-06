#!/usr/bin/python3
"""Module that define a class Rectangle
"""
Rectangle = __import__('10-square').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """Init with super function to use all attributes from parent class"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Area of a Square"""
        return self.__size * self.__size

    def __str__(self):
        """Rectangle description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
