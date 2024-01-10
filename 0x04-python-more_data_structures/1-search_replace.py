#!/usr/bin/python3
def search_replace(my_list, search, replace):

    new_list = []
    for n in my_list:
        if n == search:
            new_list += [replace,]
        else:
            new_list += [n,]

    return new_list
