#!/usr/bin/python3
"""
Function that write a string to atext file
"""


def write_file(filename="", text=""):
    """return the nuber of character written"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
