#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_num = my_list[0]
    list_len = len(my_list)

    for i in range(0, list_len):
        if my_list[i] > max_num:
            max_num = my_list[i]
    return max_num
