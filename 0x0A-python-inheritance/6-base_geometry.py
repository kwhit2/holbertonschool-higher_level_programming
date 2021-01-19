#!/usr/bin/python3
""" This module is creating the class 'BaseGeometry' with the public instance
    of the method 'def area(self):' that raises an Exception with the message
    "area() is not implemented" """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ area method:
            Args: self
            Raises: Exception
            Returns: None
        """
        raise Exception("area() is not implemented")
