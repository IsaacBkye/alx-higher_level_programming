#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    summation = 0
    argc = len(argv) - 1
    for i in range(1, argc + 1):
        summation += int(argv[i])
    print(summation)
