#!/usr/bin/python3
""" This module is adding to the class 'BaseGeometry' the public instance
    of the method 'def integer_validator(self, name, value):'
    that validates value """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ area method:
            Args: self
            Raises: Exception
            Returns: None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator method:
            Args:
                self
                name
                value
            Raises:
                TypeError
                ValueError
            Returns:
                None
        """
        if type(value) is not int:  # or: if isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return
