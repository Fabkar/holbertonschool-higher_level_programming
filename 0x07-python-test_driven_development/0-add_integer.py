#!/usr/bin/python3
"""
Function to sum integers


"""


def add_integer(a, b=98):
    """summary between two elements a and b must be \
first casted to integers if they are float

    Raises:
        TypeError: [when a is not integer]
        TypeError: [when b is not integer]

    Returns:
        [int, float]: [elements added]
    """
    if type(a) is int or type(a) is float:
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if type(b) is int or type(b) is float:
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return (a + b)
