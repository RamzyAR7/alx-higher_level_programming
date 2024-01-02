#!/usr/bin/python3
for n1 in range(0, 9):
    for n2 in range(1 + n1, 10):
        if n1 != 8 or n2 != 9:
            print("{:d}{:d}, ".format(n1, n2), end="")
        else:
            print("{:d}{:d}".format(n1, n2))
