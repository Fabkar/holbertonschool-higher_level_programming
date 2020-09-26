#!/usr/bin/python3
"""
Function to print a full name.


"""


def say_my_name(first_name, last_name=""):
    """say_my_name function print the first and last name

    Args:
        first_name (str): [only strings]
        last_name (str): [only strings].

    Raises:
        TypeError: [first name must be a string]
        TypeError: [last_name must be a string]
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
