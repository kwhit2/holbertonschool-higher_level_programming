#!/usr/bin/python3
""" Function that returns the list of available attributes
    and methods of an object """


def lookup(obj):
    """ lookup method:
        Args:
            obj: object to look up in order to return its attributes & methods
        Returns:
            attributes & methods of the object
    """
    return dir(obj)
