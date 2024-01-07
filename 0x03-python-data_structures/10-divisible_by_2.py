#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_str = []
    for n in my_list:
        list_str.append(n % 2 == 0)
    return list_str
