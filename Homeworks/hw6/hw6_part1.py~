#File: hw6_part1.py
#Author: Ati Ok
#Date: Thursday, March 24th, 2016
#Section: 15
#Email: ao10@umbc.edu
#Description: This file contains python code that reads in numbers from a user and adds them to a list.

def main():
    myList = []
    
    for i in range(0,8): #this outer loop runs 8 times for each of the 8 values in our list
        num = int(input("Please enter a number: "))
        myList.append(num)

        for j in range (0, len(myList)): #this inner loop runs 0 - however long our current list is
            if (num == myList[j] and j != 0):
                print("The number", num, "is already in the list. ")
                num = int(input("Please enter a number: "))
                myList.append(num)
    print(myList)

main()
