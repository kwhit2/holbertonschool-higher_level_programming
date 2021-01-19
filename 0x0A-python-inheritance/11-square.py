#!/usr/bin/python3
""" This module contains a class Square that inherits from Rectangle
    (9-rectangle.py). (task based on 10-square.py). It contains instantiation
    with size: 'def __init__(self, size):' The area is implemented to return
    the area of the square. str() should return the square description """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle """
    def __init__(self, size):
        """ override width & height with size """
        super().integer_validator("size", size)
        super(Square, self).__init__(size, size)
        self.__size = size

    def __str__(self):
        """ __str__ method will return size as both the width & the height """
        return ("[Square] {}/{}".format(self.__size, self.__size))
