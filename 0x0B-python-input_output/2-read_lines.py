#!/usr/bin/python3
"""
Read n lines of text file and print stdout
"""


def read_lines(filename="", nb_lines=0):
    """Class read_lines to read each by line.

    Args:
        filename (str): Name of file given.
        nb_lines (int): Number of line to read.
    """
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
