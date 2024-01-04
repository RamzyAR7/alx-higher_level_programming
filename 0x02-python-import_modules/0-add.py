#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    add_0 = __import__("add_0")
    result = add_0.add(a, b)
    add_0 = __import__("add_0")
    print("{} + {} = {}".format(a, b, add(a, b)))
