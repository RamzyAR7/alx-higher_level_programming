#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    x = set(my_list)
    new_list = list(x)

    for n in new_list:
        sum += n

    return sum
