#File:    hw7_part1.py
#Author: Ati Ok
#Date: April 3rd, 2016
#Section: 15
#Email: ao10@umbc.edu
#Description:This file contains python code that converts  a 1-800-NUMBER into numbers

def convertLetter(letter): #This function takes in a letter and returns it as an integer that represents the letter
    if (letter == 'A' or letter == 'B' or letter == 'C'):
        letter = "2"
    elif (letter == 'D' or letter == 'E' or letter == 'F'):
        letter = "3"
    elif (letter == 'G' or letter == 'H' or letter == 'I'):   #We have to change letter to a string because python
        letter = "4"                                          #can't convert integers to strings implicitly
    elif (letter == 'J' or letter == 'K' or letter == 'L'):
        letter = "5"
    elif (letter == 'M' or letter == 'N' or letter == 'O'):
        letter = "6"
    elif (letter == 'P' or letter == 'Q' or letter == 'R' or letter == 'S'):
        letter = "7"
    elif (letter == 'T' or letter == 'U' or letter == 'V'):
        letter = "8"
    elif (letter == 'W' or letter =='X' or letter == 'Y' or letter == 'Z'):
        letter = "9"
    return letter

def main():
    convertedNum = ""
    print("Welcome to the Telephone Converter!")
    phoneNum = input("Enter the phone number: ")
    phoneNum = phoneNum.upper()   #Convert the phone number to all-upper case
    for x in phoneNum:            #Traverse through our phone number element by element
        convertedNum += convertLetter(x) #Starts with a blank string then calls convertLetter() to return a number
    print(convertedNum)                  #adds that number to the blank string after the 1-800

main()
