#File: hw7_part3.py
#Author: Ati Ok
#Date: April 4th, 2016
#Section: 15
#Email: ao10@umbc.edu
#Description: This file contains python code that calculates the total number of words in a file
# the average word length in a file, and the total number of sentences in a file

def main():
    numWords = 0
    numSentences = 1
    numCharacters = 0

    fileName = input("Please enter the name of the file to open: ")
    while (fileName[-4:] != ".dat" and fileName[-4:] != ".txt"):  #Check if the file ends with a proper doc type
        print("The file must end in .txt or .dat to be valid.")   #Reprompt for a valid file 
        fileName = input("Please enter the name of the file to open: ")
    myFile = open(fileName,"r")                                   #Open the file for "r"(eading)

    for line in myFile: #This goes through the file line by line
        numWords = numWords + len(line.split()) #numWords starts at 0 but is added by the length of each line.split() array which represents words per line
        for x in line.split():                  #This counts the number of characters in the list of words
           numCharacters = numCharacters + len(x)
           for y in x:                          #Check each character to see if it is a period 
               if (y == '.'):                   #There are n sentences for (n+1) periods
                   numSentences = numSentences + 1
    


    avgLength = numCharacters / numWords
    print("On average, each word is:", avgLength, "characters long")
    print("The file", fileName,"has:", numWords, "words in it")
    print("There are", numSentences, "sentences in the file. ")
    myFile.close()  #Close the file to prevent memory leak?



main()
