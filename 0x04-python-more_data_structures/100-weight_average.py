#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    mul = 0
    sub = 0
    for x, y in my_list:
        mul += x * y
        sub += y
    if sub == 0:
        return 0
    return mul / sub
