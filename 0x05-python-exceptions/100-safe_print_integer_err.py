#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False

# Function that prints an integer.
# import sys module in order to print to stderr file
# try: print the value and return True
# except: if it is not an integer print error argument to stderr...
# ...then return False
