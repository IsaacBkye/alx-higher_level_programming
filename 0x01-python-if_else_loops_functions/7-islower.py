#!/usr/bin/python3
def islower(c):
    unixcode = ord(c)
    if unixcode >= 97 and unixcode <= 122:
        return True
    return False
