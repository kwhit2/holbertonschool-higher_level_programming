#!/usr/bin/python3
""" Function that writes an Object to a text file,
    using a JSON representation: """


import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file method:
        Args:
            my_obj: object to written to a text file using json representation
            filename: text file to be written to
        Returns:
            object to a text file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return (json.dump(my_obj, f))
