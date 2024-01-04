#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
        print("1:{}".format(argv[1]))
    else:
        print("{} arguments:".format(len(argv)))

        for i, arg in enumerate(argv[1:], start=1):
            print("{:d}: {}".format(i, arg))
