#!/usr/bin/python3
"""
this module for function that writes an Object to
a text file, using a JSON representation:
"""


import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to
    a text file, using a JSON representation:
    """

    json_str = json.dumps(my_obj)

    with open(filename, "w+") as json_file:
        json_file.write(json_str)
