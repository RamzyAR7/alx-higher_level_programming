#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    total = 0
    prev = 0
    romn_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for k in reversed(roman_string):
        current = romn_num[k]
        if prev <= current:
            total += current
        else:
            total -= current
        prev = current

    return total
