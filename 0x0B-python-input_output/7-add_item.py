#!/usr/bin/python3
"""
this module for script that adds all arguments
to a Python list, and then save them to a file
"""


import sys
from _5-save_to_json_file import save_to_json_file
from _6-load_from_json_file import load_from_json_file


def main():
    argv = sys.argv[1:]

    try:
        json_str = load_from_json_file("add_item.json")
    except FileExistsError:
        json_str = []
    
    json_str.extend(argv)
    save_to_json_file(json_str, "add_item.json")
