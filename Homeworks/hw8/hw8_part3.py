#File: hw8_part3.py
#Author: Ati Ok
#Date: April 24th, 2016
#Section: 15
#Email: ao10@Umbc.edu
#Description: This file contains python code that allows us to build a list of all unique characters in that file, using a recursive function

def newChar(fileString, uniqueList):
    #uniqueList.append(fileString)
    #print(uniqueList)
    
    if len(fileString) == 1: #Base Case; Our recursive case stops at 1
        return
    
    if (fileString[0] in uniqueList) == False: #Check if the character is in our list already
        uniqueList.append(fileString[0])
    
    if len(fileString) > 1:  #Recursive Case
        string2 = fileString[1:]
        newChar(string2, uniqueList) #Call our function again until we reach our base case
        
        
def main():
    myFile = open("input.txt", 'r')
    
    fileString = myFile.read() #Read it as one line
    uniqueList = []  
    print(fileString)
    newChar(fileString, uniqueList)
    print(uniqueList)
    
    myFile.close()
main()
