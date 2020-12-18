#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    result = []  # empty list
    for element in set_1:  # same as previous task but opposite
        if element not in set_2:  # make sure elements of set1 are not in set2
            result.append(element)
    for element in set_2:
        if element not in set_1:
            result.append(element)
    return result
