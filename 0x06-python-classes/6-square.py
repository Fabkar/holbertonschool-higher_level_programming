#!/usr/bin/python3
"""first class"""


class Square:
    """(python3 -c 'print(__import__("my_module").MyClass.__doc__)')"""
    def __init__(self, size=0, position=(0, 0)):
        """instance initializing"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """return value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """variable initializing"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """return position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """position variable initializing"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """method return current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """method to print # in all the square position"""
        if self.__size == 0:
            print()
            return
        if self.__position[1] >= 0:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
