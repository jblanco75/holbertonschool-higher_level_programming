#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        if j >= 97 and j <= 122:
            i = chr(j - 32)
        print('{:s}'.format(i), end='')
    print("")
