#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_to_remove = [k for k, v in a_dictionary.items() if v == value]

    if key_to_remove == []:
        return a_dictionary

    for k in key_to_remove:
        a_dictionary.pop(k)
    return a_dictionary
