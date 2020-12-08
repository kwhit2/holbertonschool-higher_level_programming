#!/usr/bin/python3
for i in range(0, 100):  # numbers from 0-99
    if i != 99:  # if not equal to 99
        print("{:02d}, ".format(i), end="")  # print with total of 2 digits
    else:
        print("{:02d}".format(i))  # if == 99 print 99 with no , after
