#!/usr/bin/python3
""" Function that returns True if the object is exactly an instance
    of the specified class ; otherwise False. """


def is_same_class(obj, a_class):
    """ is_same_class method:
        Args:
            obj: object to be tested if it is exactly an instance of
            the specified class
            a_class: class that is obj is being test against to verify True
            or False
        Returns:
            True if obj is exactly an instance of class or False if it is not
    """
    return (type(obj) == a_class)
