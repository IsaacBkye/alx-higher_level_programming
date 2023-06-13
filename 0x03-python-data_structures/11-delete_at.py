#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if (idx >= 0 or idx < length):
        for i, cnt in enumerate(my_list):
            if (i == idx):
                my_list.remove(i + 1)
    return (my_list)
