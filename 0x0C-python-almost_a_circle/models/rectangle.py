#!/usr/bin/python3
"""
Clase Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Init Attributes Constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @staticmethod
    def validator(name, value):
        """Validator of all setter methods and instantiation"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if name in ["width", "height"] and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        if name in ["x", "y"] and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    @property
    def width(self):
        """Getter to width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter to width"""
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter to height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter to height"""
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter to x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter to x"""
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter to y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter to y"""
        self.validator("y", value)
        self.__y = value

    def area(self):
        """Area of Rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if kwargs and len(args) == 0:
            for key, value in kwargs.items():
                if key in ['id', 'width', 'height', 'x', 'y']:
                    setattr(self, key, value)
        elif args is not None:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """Dictionary representation of rectangle"""
        keys = ['id', 'width', 'height', 'x', 'y']
        vals = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(keys, vals))

