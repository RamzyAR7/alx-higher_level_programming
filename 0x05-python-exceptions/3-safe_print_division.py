#!/usr/bin/python3
def safe_print_division(a, b):
    z = 0
    try:
        z = a/b
        return z

    except ZeroDivisionError:
        z = None
        return z
    finally:
        print("Inside result: {:f}".format(z))


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
