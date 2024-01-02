#!/usr/bin/python3
for char in map(str, range(97, 123)):
    if char == 'q' and char == 'e':
        continue
    print("{}".format(char), end="")
