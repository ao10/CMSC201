#File: hw7_part2.py
#Date: April 4th, 2016
#Section: 15
#Email: ao10@umbc.edu
#Author: Ati Ok
#Description: This file contains python code that simulates a currency exchange
#The program converts from USD to Retriever Bux and vise-versa

US_DOLLAR_RATE = 8   #Defining my constant variables / rates of conversion
RETRIEVER_BUX_RATE = 0.125

def convertToBux(usDollars): #This function takes in a floating point value that represents USD and returns 
    value = (usDollars * US_DOLLAR_RATE) #a floating point value that represents retriever bux
    value = format(value, '.2f')
    return value

def convertToUSD(retriever_bux): #This function takes in a floating point value that represents retriever bux and returns
    value = (retriever_bux * RETRIEVER_BUX_RATE) #a floating point value that represents US Dollars
    value = format(value, '.2f')
    return value

def main():

    print("Welcome to the Currency Converter!")
    print("What would you like to do?")
    print("1. Convert US Dollars to Retriever Bux")
    print("2. Convert Retriever Bux to US Dollars")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    while (choice != 1 and choice != 2 and choice != 3): #Check if the user enters a value besides 1,2, or 3
        print("That is an invalid choice.")              # and reprompt them for a proper value 
        choice = int(input("Enter your choice: "))
    numConvert = float(input("How much do you want to convert? "))

    if (choice == 1): #Convert from USD to Retriever Bux
        print(numConvert,"US Dollars equates to ",convertToBux(numConvert),"Retriever Bux ")
        print("Good bye, and thank you for using the Currency Converter!")

    elif (choice == 2): #Convert from Retriever Bux to USD
        print(numConvert,"Retriever Bux equates to ",convertToUSD(numConvert),"US Dollars")
        print("Good bye, and thank you for using the Currency Converter!")
 
    else: #Print goodbye!
        print("Good bye, and thank you for using the Currency Converter!")


main()
