#!/usr/bin/python3
"""the object is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """
    Returns:
        Check if object inherits from a class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
