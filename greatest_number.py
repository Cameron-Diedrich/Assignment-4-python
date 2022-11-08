#!/usr/bin/env python3

# Created by: Cameron Diedrich
# Created on: Nov 2022
# This program finds the greatest number of three inputs

def main():
    # Python program to find the largest number among the three input numbers

    # Input
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    print("The largest number is", largest)

    print("\nDone.")

if __name__ == "__main__":
    main()
