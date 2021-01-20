#!/usr/bin/python3
""" Function that creates an Object from a “JSON file”: """


import json


def load_from_json_file(filename):
    """ load_from_json_file method:
        Args:
            filename: json file to create object from
        Returns:
            object created from json file
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return (json.load(f))
