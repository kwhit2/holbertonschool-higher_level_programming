#!/usr/bin/python3
def safe_print_division(a, b):
    answer = 0
    try:
        answer = a / b
        return (answer)
    except ZeroDivisionError:
        answer = None
        return
    finally:
        print("Inside result: {}".format(answer))

# Function that divides 2 integers and prints the result.
# set answer/result to 0
# try: set answer to the result of a divided b
# return answer/result
# except: if there is a zerodivisionerror, answer is set to None & returned
# finally: print the answer/result of division
