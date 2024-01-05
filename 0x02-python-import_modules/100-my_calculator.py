#!/usr/bin/python3
def calc():
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    argc = len(argv) - 1

    if argc == 3:

        if argv[2] not in {'+', '-', '*', '/'}:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]
        result = 0

        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = sub(a, b)
        elif operator == '/':
            result = div(a, b)
        elif operator == '*':
            result = mul(a, b)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    calc()
