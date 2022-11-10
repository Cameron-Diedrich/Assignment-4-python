#!/usr/bin/env python3

# Created by: Cameron Diedrich
# Created on: Nov 2022
# This program finds the greatest number of three inputs

def main():
    # Python program to find the largest number among the three input numbers

    # Input
    firstNumber = float(input("Enter first number: "))
    secondNumber = float(input("Enter second number: "))
    thirdNumber = float(input("Enter third number: "))

    # process and output
    if (firstNumber >= secondNumber) and (firstNumber >= thirdNumber):
        largest = firstNumber
    elif (secondNumber >= firstNumber) and (secondNumber >= thirdNumber):
        largest = secondNumber
    else:
        largest = thirdNumber

    print("The greatest number is", largest)

    print("\nDone.")

if __name__ == "__main__":
    main()
