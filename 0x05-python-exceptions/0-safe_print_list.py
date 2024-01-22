#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    z = 0

    try:
        for n in my_list:
            if x > 0:
                print("{}".format(n), end="")
                x -= 1
                z += 1
        print()

    except IndexError:
        print()

    return z
