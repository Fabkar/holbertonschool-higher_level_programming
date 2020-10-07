#!/usr/bin/python3
"""Class Base Geometry
"""


class BaseGeometry:
    """method based in Geometry"""
    def area(self):
        """area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer Validator
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
