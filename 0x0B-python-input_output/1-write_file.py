#!/usr/bin/python3
"""
this module for  function that writes a string to a text file (UTF8) and
returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8) and
    returns the number of characters written:
    """

    with open(filename, "w", encoding="utf-8") as file:
        num_of_bytes = file.write(text)

    return num_of_bytes
