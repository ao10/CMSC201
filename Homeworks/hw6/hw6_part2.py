#File: hw6_part2.py
#Author: Ati Ok
#Date: 3/28/2016
#Section: 15
#Email: ao10@umbc.edu
#Description: This file contains python code that uses a very simple algorithm to compute
#the prime numbers up to 500

def main():
    myList = [] #initialize an empty list
    for x in range(2,501): #Run the loop starting at 2 and ending at 500
        myList.append(x)
        if (x != 2 and x % 2 == 0): #remove all multiples of 2 
            myList.remove(x)
        elif (x != 3 and x % 3 == 0): #remove all multiples of 3
            myList.remove(x)
        elif(x != 5 and x % 5 == 0): #remove all multiples of 5 
            myList.remove(x)
        elif(x != 7 and x % 7 == 0):
            myList.remove(x)
        elif(x != 11 and x % 11 == 0):
            myList.remove(x)
        elif(x != 13 and x % 13 == 0):
            myList.remove(x)
        elif(x != 17 and x % 17 == 0):
            myList.remove(x)
        elif(x != 23 and x % 23 == 0):
            myList.remove(x)


    for i in myList:
        print(i, end = " ")


    ###### This was the other implementation I had but I couldn't figure out why it was out of bounds #######
    
    #for x in range(2, 501):
    #    myList.append(x)
    #    if (x != 2 and x % 2 == 0):
    #        myList.remove(x)
    #    for y in range(3, 25, 2):
    #        if (myList[x] % y == 0):
    #            myList.remove(x)
    #print(myList)








main()
