#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:  # if the key passed is in the dictionary
        del a_dictionary[key]
    return a_dictionary
