#File: hw5_part3.py
#Author: Ati Ok
#Date: Sunday, March 6th , 2016
#Section: 15
#Email: ao10@umbc.edu
#Description: This program takes in a phone number as input and outputs it in a new, standard format

def main():
    phoneNum = input("Please enter the phone number: ")

    if (phoneNum[0] == "("):  #Check if the phone number is in format number 1 by checking for parentheses
        newNum = phoneNum[0:5] + " " + phoneNum[5:8] + phoneNum[8:] #Concatenate the old format and slice it
        print(newNum)

    elif (phoneNum[3] == '-'): #Check if the phone number is in format number 2 by checking for a hyphen
        newNum = "(" + phoneNum[0:3] + ")" + " " + phoneNum[4:7] + "-" + phoneNum[8:]
        print(newNum)
    
    else:
        newNum = "(" + phoneNum[0:3] + ")" +" " + phoneNum[3:6] + "-" + phoneNum[6:]
        print(newNum)

main()
