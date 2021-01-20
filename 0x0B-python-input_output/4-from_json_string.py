#!/usr/bin/python3
""" Function that returns an object (Python data structure)
    represented by a JSON string: """


import json


def from_json_string(my_str):
    """ from_json_string method:
        Args:
            my_str: json string to be converted into an object
        Returns:
            object represented by the json string
    """
    return (json.loads(my_str))
