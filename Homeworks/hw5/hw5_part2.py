#File: hw5_part2.py
#Author: Ati Ok
#Date: March 4th, 2016
#Email: ao10@umbc.edu
#Section: 15
#Description: This program tells the user the cost of making copies at the UMBC copy center
# , which uses a sliding scale for pricing copies

def main():
    FIRST_100 = 0.08   #Setting up final constants
    NEXT_900 = 0.06
    NEXT_9000 = 0.05
    AFTER_10000 = 0.04

    numCopies = int(input("How many copies do you want? "))
    if (numCopies <= 100):
        totalCopies = numCopies * FIRST_100    #Multiply number of copies by the copy rate of FIRST_100
        print("The total cost for",numCopies,"copies is: $",totalCopies)
    
    elif (numCopies > 100 and numCopies < 900): #Add the first 100 copies and the rate of the next 900 copies
        totalCopies = (100 * FIRST_100) + ((numCopies - 100) * NEXT_900)
        print("The total cost for", numCopies,"copies is: $", totalCopies)
    
    elif (numCopies > 100 and numCopies > 900 and numCopies < 9000): #Add the first 100, next 900, and next 9000
        totalCopies = (100*FIRST_100) + (NEXT_900*900) + ((numCopies - 1000) * NEXT_9000)
        print("The total cost for", numCopies,"copies is: $", totalCopies)

    else:   #Add the first 100 copies, then the next 900, the next 9000, and finally the next 10,000 copies
        totalCopies = (100*FIRST_100) + (NEXT_900*900) + (NEXT_9000 * 9000) + ((numCopies - 10000)*AFTER_10000)
        print("The total cost for", numCopies,"copies is: $", totalCopies)


main()
