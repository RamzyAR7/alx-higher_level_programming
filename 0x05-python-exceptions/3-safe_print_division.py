#!/usr/bin/python3
def safe_print_division(a, b):
    z = 0
    try:
        z = a/b

    except ZeroDivisionError:
        z = None
    finally:
        print("Inside result: {:f}".format(z))
    return z
