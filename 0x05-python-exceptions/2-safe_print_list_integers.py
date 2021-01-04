#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            i += 1
        except (ValueError, TypeError):
            j += 1
            continue
    print()
    return (i)

# Function that prints the first x elements of a list and only integers.
# i = counter variable to keep count correct which will be returned
# for loop iterates through list to index x
# try: print the value if an integer, increment i/count
# except: value is not an integer, increment index to skip str element...
# ...then continue iterating through index until x
# print newline
# return i/count
