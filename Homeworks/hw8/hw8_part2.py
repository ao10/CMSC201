#File: hw8_part2.py
#Author: Ati Ok
#Date: April 23rd, 2016
#Section: 15
#Email : ao10@Umbc.edu
#Description: This file contains python code where a recursive function prints a hollow square

def hollowSquare(squareHeight, symbol, currentNum): 
    #currentNum = squareHeight #We use this as a counter for our square's height
    #Base Case
    if (currentNum == 0):
        return
    #Recursive Case; this will run until we reach the very last row of our square (i.e. height == 0)
    else:
        if (currentNum == squareHeight): #This prints the first & last lines as "squareHeight" amount of symbols
            print(symbol * squareHeight)
            return hollowSquare(squareHeight, symbol, currentNum - 1) #Calls itself again so the function does not end
        elif (currentNum != squareHeight): #Prints the hollow part of the square if its not the first/last line
            print(symbol + (" "*squareHeight) + symbol)
            return hollowSquare(squareHeight, symbol, currentNum - 1)
    
    
    


def main():
    height = int(input("Please enter the height of your square: "))
    while (height <= 0): #Input Validation #Make sure the user enters a valid positive value
        height = int(input("Please enter the height of your square (must be > 0): "))

    symbol = input("Please enter a character for your square: ")

    currentNum = height #We set currentNum to height in the main function because if we do it in hollowSquare()
    hollowSquare(height, symbol, currentNum) #the value of currentNum resets
    
    
main()
