#File:      hw3_part1.py
#Author:    Ati Ok
#Date:      February 18th, 2016
#E-mail:    ao10@umbc.edu
#Section:   15
#Desc:      This file contains python code to compare floating point values.

def main():
    num = float(input("Please enter a floating point number: "))    
    if (num > 0):
        print("The number", num, "is positive.")
    
    elif (num < 0):
        print("The number", num, "is negative.")

    else:
        print("The number", num, "is equal to zero.")
main()
