#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = ()

    for n1 in set_1:
        for n2 in set_2:
            if n1 == n2:
                new_list += (n1,)

    return new_list
