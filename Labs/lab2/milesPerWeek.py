#File:     milesPerWeek.py
#Author:   Ati Ok
#Date:     February 16th, 2016
#Section:  15
#E-mail:   ao10@umbc.edu
#Description: This file contains python code for milesPerWeek.py file

def main():
    VELOCITY = int(65)
    miles_trip = int(input("How many miles is your trip one-way? "))
    days = int(input("How many days a week do you go to work? "))

    milesPerWeek  = (miles_trip) * 2 * (days)
    hoursInCar = (milesPerWeek) / (VELOCITY)
    
    print("You drive about", milesPerWeek, "miles in a typical week.")
    print("At 65 mph, you spend about", hoursInCar, "hours commuting in a typical week.")

main()
