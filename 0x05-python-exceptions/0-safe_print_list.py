#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        iter = 0
        for i in range(x):
            print('{}'.format(my_list[i]), end='')
            iter += 1
        print()
        return iter
    except:
        print()
        return iter
