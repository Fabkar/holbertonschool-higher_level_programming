#!/usr/bin/python3
"""
script that adds all arguments to a Python list
"""
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file = "add_item.json"
try:
    new_file = load_from_json_file(file)
except (FileExistsError, FileNotFoundError, ValueError):
    new_file = []
for arg in sys.argv[1:]:
    new_file.append(arg)
save_to_json_file(new_file, file)
