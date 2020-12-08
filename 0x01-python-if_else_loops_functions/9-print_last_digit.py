#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)  # abs value needed for negative numbers
    print((number % 10), end="")  # print the last digit with no \n
    return (number % 10)  # return last digit
