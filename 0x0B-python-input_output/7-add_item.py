#!/usr/bin/python3
""" Script that adds all arguments to a Python list,
    and then save them to a file: Using previous functions:
    5-save_to_json_file.py & 6-load_from_json_file.py """


import json
from sys import argv

save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    new_file = load_json(filename)
except (ValueError, FileNotFoundError):
    new_file = []

new_file = new_file + argv[1:]
save_json(new_file, filename)
