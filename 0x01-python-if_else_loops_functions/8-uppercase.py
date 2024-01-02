#!/usr/bin/python3

def uppercase(str):
    for s in str:
        if ord('a') <= ord(s) <= ord('z'):
            upper = ord(s) - 32
            print("{}".format(chr(upper)), end="")
        else:
            print("{}".format(s), end="")
    print()
