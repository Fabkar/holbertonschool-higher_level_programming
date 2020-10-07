#!/usr/bin/python3
"""
Module defines a class Myint
"""


class MyInt(int):
    """
    Define class MyInt
    """
    def __int__(self, value=0):
        """
        Init MyInt
        """
        self.__value = value

    def __eq__(self, value):
        """
        compare using == operators inverted
        """
        return not self.__value == value

    def __ne__(self, value):
        """
        compare using != operators inverted
        """
        return not self.__value != value
