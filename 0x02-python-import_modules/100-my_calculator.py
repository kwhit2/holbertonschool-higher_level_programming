#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    index = len(argv)  # index is set to length of args

    if index != 4:  # index has to be atleast 3 args
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    else:
        operator = argv[2]  # operator set to operator +, -, *, /
        a = int(argv[1])  # arg1 digit(s)
        b = int(argv[3])  # arg2 digit(s)

        if operator == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))

        elif operator == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))

        elif operator == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))

        elif operator == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))

        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
