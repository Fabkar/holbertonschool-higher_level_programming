#!/usr/bin/python3
"""
Function to save an object in a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj: the object to save
        filename: file where store the object
    """
    with open(filename, mode="w", encoding='utf-8') as f:
        return json.dump(my_obj, f)
