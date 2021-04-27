#!/usr/bin/python3
for c in range(0, 10):
    for d in range(0, 10):
        if c == 8 and d == 9:
            print('{:d}{:d}'.format(c, d))
        elif c < d:
            print('{:d}{:d}, '.format(c, d), end='')
