#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

# Function that prints an integer with "{:d}".format().
# try: print the value and return True
# except: if it is not an integer return False
