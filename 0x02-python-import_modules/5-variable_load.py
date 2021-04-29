#!/usr/bin/python3
import sys
from variable_load_5 import a

if __name__ == '__main__':
    if (len(sys.argv) - 1) == 0:
        print(a)
    else:
        print(sys.argv)
