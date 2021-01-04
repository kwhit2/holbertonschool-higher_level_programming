#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            i += 1
        except IndexError:
            break
    print()
    return (i)

# Function that prints x elements of a list
# i = counter variable to keep count correct which will be returned
# for loop iterates through list to index x
# print value of each element
# add to count only if index doesn't exceed length of list
