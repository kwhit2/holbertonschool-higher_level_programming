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

    def to_json(self, attrs=None):
        """ to_json method:
            Args:
                self: object to be returned as dict (dictionary) description
                attrs: attributes
            Returns:
                the dictionary description with simple data structure
                (list, dictionary, string, integer and boolean) for
                JSON serialization of an object
        """
        if attrs is None:
            return (self.__dict__)
        return ({key: value for key, value in self.__dict__.items()
                if key in attrs})

    def reload_from_json(self, json):
        """ reload_from_json method:
            Args:
                self: self
                json: dictionary that replaces all attributes of the...
                    ...student instance
            Returns:
                None
        """
        self.__dict__.update(json)
