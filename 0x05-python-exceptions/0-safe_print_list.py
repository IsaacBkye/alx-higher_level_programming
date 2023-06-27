#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    _print = 0
    try:
        for a in range(0, x):
            print(my_list[a], end="")
            _print += 1
    except IndexError:
        None
    print()
    return (_print)
