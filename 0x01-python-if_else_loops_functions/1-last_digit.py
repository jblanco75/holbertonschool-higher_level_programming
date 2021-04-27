#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = (number * - 1) % 10
else:
    last = number % 10
str1 = "and is greater than 5"
str2 = "and is less than 6 and not 0"
if last > 5:
    print('Last digit of {:d} is {:d} {:s}'.format(number, last, str1))
elif last == 0:
    print('Last digit of {:d} is 0 and is 0'.format(number))
else:
    print('Last digit of {:d} is {:d} {:s}'.format(number, last, str2))
