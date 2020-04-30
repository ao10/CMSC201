#File: hw5_part1.py
#Author: Ati Ok
#Date: March 4th, 2016
#Section: 15
#Email: ao10@umbc.edu
#Description: Program that helps calculate the tip at a restaurant, given bill, and service of waiter

def main():
    totalBill = float(input("What is the total bill? "))
    serviceLevel = input("What was the level of service? ")
    while (serviceLevel != "excellent" and serviceLevel != "good" and serviceLevel != "bad"): #loop runs until user
        print("Please choose excellent, good, or bad: ")                                #chooses one of the options
        serviceLevel = input("What was the level of service? ")

    if (serviceLevel == "excellent"):   #if service is excellent tip is 25%
        tipAmount = totalBill * (0.25)
    elif (serviceLevel == "good"):  #if service is good tip is 20%
        tipAmount = totalBill * (0.20)
    else:
        tipAmount = 2  #if service is bad, tipAmount has to be $2 as a minimum
    
    print("The bill was $",totalBill)
    print("The service was",serviceLevel)
    print("The tip is $",tipAmount)
    print("The grand total with tip is: $",totalBill+tipAmount)

main()
