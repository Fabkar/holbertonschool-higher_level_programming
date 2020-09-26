#!/usr/bin/python3
"""
Function to print a square using "#"

"""

def print_square(size):
    """print_square to print a square depend by size variable.

    Args:
        size (int): [Element must be integer]

    Raises:
        TypeError: [size must be an integer]
        ValueError: [size must be >= 0]
        TypeError: [size must be an integer]
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for i in range(size):
            print("#", end='')
        print()
