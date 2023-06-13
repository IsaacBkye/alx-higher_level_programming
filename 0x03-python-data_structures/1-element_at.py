#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if (idx > length - 1 or idx < 0):
        return (None)
    for i, e in enumerate(my_list):
        if (idx == i):
            return (e)
