#!/usr/bin/python3
def common_elements(set_1, set_2):

    result = []  # empty list
    for element in set_1:  # checks all chars of set 1
        if element in set_2:  # checks all chars of set 2
            result.append(element)  # add matching chars (C) and
    return result                   # adds/appends to result which is returned

#    if (set_1 & set_2):
#        print(set_1 & set_2)
# close but not right output...curly brackets instead of []
