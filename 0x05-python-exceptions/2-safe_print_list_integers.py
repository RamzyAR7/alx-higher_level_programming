#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    z = 0
    for idx in range(0, x):
        try:
            if isinstance(my_list[idx], int):
                print("{:d}".format(my_list[idx]))
                z += 1
            print()

        except IndexError:
            print("list index out of range")
    return z
