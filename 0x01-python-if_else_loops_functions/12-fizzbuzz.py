#!/usr/bin/python3
def fizzbuzz():
    for a in range(101):
        if a % 5 == 0:
            print("Buzz", end=" ")
        elif a % 3 == 0:
            print("Fizz ", end=" ")
        else:
            print("{}".format(a), end=" ")
