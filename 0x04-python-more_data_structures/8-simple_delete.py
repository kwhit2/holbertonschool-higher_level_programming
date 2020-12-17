#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:  # if the dictionary exists
        del a_dictionary[key]
    return a_dictionary
