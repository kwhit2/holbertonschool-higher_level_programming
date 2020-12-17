#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {x: a_dictionary[x] * 2 for x in a_dictionary}

#  Below also gets correct output
#  newdict = dict(a_dictionary)
#  for value in newdict:
#      newdict[value] *= 2
#  return newdict
