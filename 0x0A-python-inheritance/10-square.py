#!/usr/bin/python3
""" This module contains a class Square that inherits from Rectangle
    '(9-rectangle.py):' It contains instantiation with size:
    'def __init__(self, size):'. The area is implemented to return
    the area of the square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Rectangle class """
    def __init__(self, size):
        """ init method:
            Args:
                self
                size (int)
            Returns:
                None
        """
        super().integer_validator("size", size)
        super().integer_validator("size", size)
        self.__size = size
        self.__size = size

    def area(self):
        """ area method for a square:
            Args:
                size (int)
            Returns:
                Area of square as int: size * size
        """
        return (self.__size * self.__size)
# Also gives correct output: return ("{}".format(self.__size * self.__size))

    def __str__(self):
        """ __str__ method:
            Args:
                size (int)
            Returns:
                Area of square
        """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
