#!/usr/bin/python3
"""
this module for function that reads a text file
"""


def read_file(filename=""):
    """
     function that reads a text file (UTF8) and prints it to stdout:
    """
    with open(filename) as file:
        print(file.read(), end="")
