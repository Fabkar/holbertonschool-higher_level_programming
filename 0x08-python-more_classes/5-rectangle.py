#!/usr/bin/python3
"""This Rectangle class"""


class Rectangle:
    """Show the attribute of rectangle"""
    def __init__(self, width=0, height=0):
        """init of attribute

        Args:
            width (int): [Width of the rectangule]. Defaults to 0.
            height (int): [height of the rectangule]. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter to width

        Returns:
            [int]: [width of rectangle]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter to width

        Args:
            value (Int): [Value of width]

        Raises:
            ValueError: [width must be higher that 0]
            TypeError: [value must be an integer]
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter to height

        Returns:
            [int]: [height of rectangle]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height

        Args:
            value (int): [value to height]

        Raises:
            ValueError: [value must be higher that 0]
            TypeError: [the value must be an integer]
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle

        Returns:
            [int]: [the area of rectangle]
        """
        return self.height * self.width

    def perimeter(self):
        """perimeter of rectangle

        Returns:
            [int]: [perimeter of rectangle]
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.height) + (2 * self.width)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        Rect = ""
        for i in range(self.height):
            Rect += "#" * self.width
            Rect += "\n"
        return Rect[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
