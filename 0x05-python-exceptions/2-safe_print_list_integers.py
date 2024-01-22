#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    z = 0
    try:
        for idx in range(0, x):
            if type(my_list[idx]) is int:
                print("{}".format(my_list[idx]))
                z += 1
        print()

    except IndexError:
        print("list index out of range")

    return z
