#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number
if number < 0:
    x = number * -1
ldigt = number % 10
if ldigt > 5:
    print(f'Last digit of {x} is {ldigt} and is greater than 5')
elif ldigt == 0:
    print(f'Last digit of {x} is {ldigt} and is 0')
elif ldigt < 6 and ldigt != 0:
    print(f'Last digit of {x} is {ldigt} and is less than 6 and not 0')
