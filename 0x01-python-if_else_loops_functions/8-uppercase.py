#!/usr/bin/python3

def uppercase(str):
    for s in str:
        if ord('a') <= ord(s) <= ord('z'):
            upper = ord(s) - 32
            print("{}".format(str(upper)), end="")
        else:
            print("{}".format(s), end="")
