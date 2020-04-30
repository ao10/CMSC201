#File: hw8_part1.py
#Date: April 22nd, 2016
#Section: 15
#Email: ao10@umbc.edu
#Author: Ati Ok
#Description: This file contains python code that allows the user to enter 
# a list of values and returns the biggest value using recursion

def maxInt(myList): #This function takes in a list of positver integers and prints the max value
    #print("Here is your list: ", myList)
    #for i in range(len(myList)): #Solving it using a for loop and no recursion
    #    if (myList[i] > max):
    #        max = myList[i]
    #print("The max value is: ", max)

    if (len(myList) == 1):  
        return myList[0]    #If theres only one value in the list it returns the first value

    else:                   
        max = maxInt(myList[1:])   #Recursive Case
                                   #This sets max to equal the list excluding the first element
        if (max > myList[0]): #Base Case
            return max
        else:            #Returns the first element if the first element is the largest
            return myList[0]
            
    

def main():
    myList = []
    userValue = 0
    while(userValue != -1):  #Loop exits when user enters -1 
        userValue = int(input("Enter a number to append to the list, or -1 to stop: "))
        if (userValue != -1): #Append every value the user enters that isn't -1
            myList.append(userValue)
    print("Here is the greatest value: ", maxInt(myList))



main()
