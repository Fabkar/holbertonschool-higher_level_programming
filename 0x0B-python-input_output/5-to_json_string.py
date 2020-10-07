#!/usr/bin/python3
"""
the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """Change object to string

    Args:
        my_obj given.
    """
    return json.dumps(my_obj)
