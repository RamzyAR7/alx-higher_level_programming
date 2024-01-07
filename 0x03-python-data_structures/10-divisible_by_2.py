#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_str = []
    for n in my_list:
        if n % 2 == 0:
            list_str += ["True",]
        else:
            list_str += ["False",]
    return list_str
