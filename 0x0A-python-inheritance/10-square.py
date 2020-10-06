#!/usr/bin/python3
"""Module that define a class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square that inherits from Rectangle
    """
    def __init__(self, size):
        """Init with super function to use all attributes from parent class
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
