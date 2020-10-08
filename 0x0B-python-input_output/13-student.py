#!/usr/bin/python3
"""
Student to disk and reload
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """Initialization of attributes

        Args:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        a dictionary representation
        """
        if attrs is None:
            return self.__dict__
        else:
            dicc = {}
            for i in self.__dict__:
                if i in attrs:
                    dicc[i] = self.__dict__[i]
            return dicc

    def reload_from_json(self, json):
        """
        Define a Student
        """
        for i in self.__dict__:
                if i in json:
                    self.__dict__[i] = json[i]
