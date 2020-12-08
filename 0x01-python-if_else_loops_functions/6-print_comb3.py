#!/usr/bin/python3
for i in range(0, 8):  # setting range for first digit to 0-7
    for j in range(i + 1, 10):  # set 2nd digit range 1-9.j 1 digit ahead of i
        print("{:d}{:d}".format(i, j), end=", ")  # printing both digits
print("{:d}{:d}".format(i + 1, j))  # printing 89 with a \n
