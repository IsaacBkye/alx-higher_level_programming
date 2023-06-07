#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        unixcode = ord(str[i])
        if unixcode >= 97 and unixcode <= 122:
            unixcode = unixcode - 32
        print("{:c}".format(unixcode), end="")
    print()
