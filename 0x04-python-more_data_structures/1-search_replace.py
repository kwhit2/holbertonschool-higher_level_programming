#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = my_list[:]

    for x in range(len(my_list)):
        if newlist[x] == search:
            newlist[x] = replace
    return newlist

# return [(replace if x == search else x) for x in my_list]
