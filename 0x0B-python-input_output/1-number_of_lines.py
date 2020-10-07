#!/usr/bin/python3
"""
Function that return the of lines of text file
"""


def number_of_lines(filename=""):
    """
    Returns:
        Number of line
    """
    with open(filename, encoding='utf-8') as f:
        return len(f.readlines())
