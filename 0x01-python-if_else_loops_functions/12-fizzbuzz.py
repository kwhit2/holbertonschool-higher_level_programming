#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):  # for numbers 1-100
        if i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i == 99:  # to get \n at end
            print(i)
        else:
            print(i, end=" ")  # for numbers not divisible by 3 0r 5
