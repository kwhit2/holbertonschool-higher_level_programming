#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return (my_list)
    else:
        for x in range(len(my_list)):
            if x is idx:
                my_list[x] = element
        return (my_list)
