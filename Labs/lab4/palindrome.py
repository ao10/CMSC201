#File: palindrome.py
#Author: Ati Ok
#Date: February 29th, 2016
#Section: 15
#E-mail: ao10@umbc.edu
#Description: This file takes in a string and checks to see if it is a
#palindrome or not

def main():
    string = input("Enter a string: ")
    palindrome = []
    for x in range(len(string) - 1, -1, -1):
        palindrome.append(string[x])
    print(palindrome)

    #palindrome checker
    stringList = []
    for x in string:
        stringList.append(x)
    print(stringList)

    if (stringList == palindrome):
        print("This is a palindrome.")
    else:
        print("This is not a palindrome.")

main()





