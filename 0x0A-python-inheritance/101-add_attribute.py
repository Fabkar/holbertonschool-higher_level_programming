#!/usr/bin/python3
"""
Add new attribute
"""


def add_attribute(obj, name, value):
    """
    update and add an attribute of an object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
