#!/usr/bin/python3
"""
this module for function that appends a string at the end of
a text file (UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added:
    """

    with open(filename, "a", encoding="utf-8") as file:
        num_of_bytes = file.write(text)

    return num_of_bytes
