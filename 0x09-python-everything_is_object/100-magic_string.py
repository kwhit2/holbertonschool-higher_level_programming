#!/usr/bin/python3
def magic_string(str=[]):
    str.append("Holberton")  # this also works: str += ["Holberton"]
    return (", ".join(str))
