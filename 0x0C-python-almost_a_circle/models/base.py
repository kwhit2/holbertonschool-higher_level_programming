#!/usr/bin/python3
""" This module contains a class Base """


import json


class Base:
    """ Base class: Contains private class attribute __nb_objects = 0 """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """ __init__ method: a class constructor. Checks for id
        Args:
            self:
            id: Assume id is an integer. Do not need to test the type of...
            ...it(id). Default value of id is set to None
        Return:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string method:
                returns the JSON string representation of list_dictionaries
            Args:
                list_dictionaries: a list of dictionaries
            Returns:
                "[]" if list_dictionaries is empty or None. Otherwise...
                ...returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries is "[]":
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_json_file method:
                Args:
                    cls: class
                    list_objs: list of objects
                Returns:
                    object to a text file
        """
        filename = cls.__name__ + ".json"  # makes Rectangle.json & Square.json
        new_obj = []  # create empty list object
        if list_objs is not None:
            for a in list_objs:
                new_obj.append(cls.to_dictionary(a))
                # ^ convert list_objs to dictionary and store it in new_obj
        with open(filename, mode='w', encoding='utf-8') as new_file:
            new_file.write(cls.to_json_string(new_obj))
            # ^ convert new_obj dict into json string & write that to the file

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string method:
                returns the list of the JSON string representation json_string:
            Args:
                json_string: is a string representing a list of dictionaries
            Returns:
                If json_string is None or empty, return an empty list.
                Otherwise, return the list represented by json_string.
        """
        if json_string is None or json_string is "[]":
            return "[]"
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ create method:
                returns an instance with all attributes already set
            Args:
                **dictionary: can be thought of as a double pointer to...
                ...a dictionary that holds the values of the attributes...
                ...we are to assign
                cls: class
            Returns:
                An instance with all attributes already set
        """
        if cls.__name__ is "Rectangle":  # check if class is Rectangle
            dummy = cls(6, 9)  # assign it 2 arguments for height & width
        if cls.__name__ is "Square":  # check if class is Square
            dummy = cls(69)  # assign it 1 argument for size
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """ load_from_file:
                returns a list of instances
            Args:
                cls: class
            Returns:
                a list of instances
        """
        filename = cls.__name__ + ".json"
        new_obj = []
        try:
            with open(filename, mode='r', encoding='utf-8') as new_file:
                new_obj = cls.from_json_string(new_file.read())
            for i, j in enumerate(new_obj):
                new_obj[i] = cls.create(**new_obj[i])
        except:
            pass
        return (new_obj)

#  try to open file to read it (if it doesn't exist, "pass" is enacted...
#  ...and then our empty list (new_obj) is returned)
#  set the list of the json string representation of the contents of the file..
#  ...equal to new_obj
#  iterate through new_obj and assign the value at each key to the values...
#  ...read from the file
