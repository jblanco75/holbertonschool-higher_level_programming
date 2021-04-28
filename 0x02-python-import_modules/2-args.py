#!/usr/bin/python3
import sys

n = len(sys.argv)

if (n - 1) > 1:
    print('{:d} arguments:'.format(n - 1))

if (n - 1) == 1:
    print('{:d} argument:'.format(n - 1))

if (n - 1) == 0:
    print('{:d} arguments.'.format(n - 1))

for i in range(1, n):
    print('{} : {}'.format(i, sys.argv[i]))
