#!/usr/bin/python3
def calc():
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in {'+', '-', '*', '/'}:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    value = match_calc(argv)
    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], value))


def match_calc(argv):
    from calculator_1 import add, sub, mul, div

    match argv[2]:
        case '+':
            return add(int(argv[1]), int(argv[3]))
        case '-':
            return sub(int(argv[1]), int(argv[3]))
        case '*':
            return mul(int(argv[1]), int(argv[3]))
        case '/':
            return div(int(argv[1]), int(argv[3]))


if __name__ == "__main__":
    calc()
