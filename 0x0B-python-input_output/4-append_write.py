#!/usr/bin/python3
"""
function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """Class append_write to appends a string

    Args:
        filename (str): Name of file given.
        text (str): String to add.
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
