#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

def calc():
    argc = len(argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in {'+', '-', '*', '/'}:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    result = match_calc(a, b, operator)

    print("{} {} {} = {}".format(a, operator, b, result))

def match_calc(a, b, operator):
    match operator:
        case '+':
            return add(a, b)
        case '-':
            return sub(a, b)
        case '*':
            return mul(a, b)
        case '/':
            return div(a, b)

if __name__ == "__main__":
    calc()
