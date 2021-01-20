#!/usr/bin/python3
""" This module contains a class student that defines a student """


class Student():
    """ class Student """
    def __init__(self, first_name, last_name, age):
        """ __init__ method:
            Args:
                self
                first_name (string)
                last_name (string)
                age (int)
            Returns:
                None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ to_json method:
            Args:
                self: object to be returned as dict (dictionary) description
            Returns:
                the dictionary description with simple data structure
                (list, dictionary, string, integer and boolean) for
                JSON serialization of an object
        """
        return (self.__dict__)
