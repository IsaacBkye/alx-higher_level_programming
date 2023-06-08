#!/usr/bin/python3
def fizzbuzz():
    for a in range(101):
        if a % 5 == 0:
            print("Buzz ")
        elif a % 3 == 0:
            print("Fizz ")
        else:
            print("{}".format(a), end=" ")
