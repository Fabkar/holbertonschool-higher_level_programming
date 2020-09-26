#!/usr/bin/python3
"""
Function to print a text with 2 new lines in a specific characters

"""


def text_indentation(text):
    """Function to replace a specific characters to 2 new lines.

    Args:
        text (str): [Is a string]

    Raises:
        TypeError: [text must be a string]
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('. ', '.\n\n')
    text = text.replace('? ', '?\n\n')
    text = text.replace(': ', ':\n\n')
    print(text, end="")
