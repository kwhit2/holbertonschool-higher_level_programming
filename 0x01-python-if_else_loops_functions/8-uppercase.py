#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):  # end of range is end string length
        char = ord(str[i])  # convert char into int for ASCII comparison
        if char >= 97 and char <= 122:  # if lowercase
            char = char - 32  # convert to uppercase
        print("{}".format(chr(char)), end="")  # use chr to return ASCII to char
    print()  # print \n
