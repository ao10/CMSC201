#File : hw4_part4.py
#Author: Ati Ok
#Date: February 22nd , 2016
#Email : ao10@umbc.edu
#Section: 15
#Description: This file contains python code measuring temperature and states of matter

def main():
    temp = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celcius, or 'F' for Fahrenheit: ")
     
    if (scale == 'C'):  #water
        if (temp > 0 and temp < 100):
            print("At this temperature, water is a liquid.")
        elif (temp <= 0): #solid
            print("At this temperature, water is a solid.")
        elif (temp >= 100):
            print("At this temperature, water is a gas.")

    elif (scale == 'F'):
        if (temp > 212):
            print("At this temperature, water is a gas.")
        elif (temp < 32):
            print("At this temperature, water is a solid.")
        elif (temp < 212 and temp > 32):
            print("At this temperature, water is a liquid.")


main()
