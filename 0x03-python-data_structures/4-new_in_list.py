#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    newList = list(my_list)
    if (idx >= 0 or idx < length):
        for i, cnt in enumerate(newList):
            if (i == idx):
                newList[i] = element
    return (newList)
