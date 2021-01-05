#!/usr/bin/python3
""" This module contains a class Square """


class Square:
    """ Square class. Represents a square

    Attributes:
        __size (int): size of 1 side of square
    """
    def __init__(self, size):
        """ Initializes the square

        Args:
            size (int): size of 1 side of square

        Return: None
        """
        self.__size = size
