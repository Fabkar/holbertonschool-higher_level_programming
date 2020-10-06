#!/usr/bin/python3
"""
function to listing of avalible attributes and methods of an object

"""


def lookup(obj):
    """Returns the list of available attributes and methods of an
    object
    """
    return dir(obj)
