#File: proj2.py 
#Author: Ati Ok  
#Date: Wednesday, May 4th, 2016 
#Section: 15 
#E-mail: ao10@umbc.edu 
#Description: This file contains python code that contains a recursive word search

###################################################################################################################
def printPuzzle(puzzle): #This function takes in our 2D-list puzzle as a parameter 
    #for i in range(len(puzzle)):   #and it prints it out in the layout of a word-search
    #    print(puzzle[i])
        
    for row in puzzle:
        for col in row:
            print(col, end = ' ')
        print(end = '\n')
    
def getPuzzle(PUZZLE): #We need to create our own board so we can call our searchWord function recursively
    puzzle = []        #This function takes in our puzzle file as a parameter and returns a 2D word-search
    for eachLine in PUZZLE:     #This loop turns each row into an element of our 'puzzle' list
        puzzle.append(eachLine)
        #GET RID OF THE SPACES TOMMOROW
        
    for i in range(len(puzzle)):  #This loop strips each '\n' character from each row/string
        if ("\n" in puzzle[i]):
            puzzle[i] = puzzle[i][0:-1]
    
    for x in range(len(puzzle)): #Get rid of the spaces in between each letter to make it easier for us 
        puzzle[x] = puzzle[x].split(' ')
    
    for j in range(len(puzzle)): #This loop casts each row/string into a list
        
        puzzle[j] = list(puzzle[j]) #Now each row is a list inside our 'puzzle' list making it a 2D-List
            
        
    return puzzle
    
def getWordList(WORD_LIST): #This function stores all the words we need to search for in a list
    wordList = []           #It takes in our WORD_LIST file as a parameter and returns a list of words to search for
    for eachLine in WORD_LIST:   #Append each word into our new list
        wordList.append(eachLine)
        
    for i in range(len(wordList)): #We need to remove the \n from each word 
        if ("\n" in wordList[i]):  #We can't use .strip() because we're reading from a file so we can't alter 
            wordList[i] = wordList[i][0:-1] #the words directly so we have to use a for loop to break it off
    return wordList

###########################################################################################################################

def getFirstLetter(word, puzzle): #Returns whether the word was found (True/False) and the coordinates (Integer-Values)
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if (puzzle[i][j] == word[0]):
                print("Match for letter", word[0],  "at (row, column): ", i, ' ', j)
                firstLetter_ROW = i
                firstLetter_COL = j
                
#def findWord(firstLetter_ROW,firstLetter_COL, word, puzzle):                

    
def main():
    print("Welcome to the Word Search!")
    print("For this, you will import two files: 1. The puzzle board, and 2. The word list.")
    
    puzzle_fileName = input("What is the puzzle file you would like to import?: ")
    wordList_fileName = input("What is the word list file you would like to import?: ")
    
    PUZZLE_FILE = open(puzzle_fileName,'r') #Read in the puzzle file
    WORD_LIST = open(wordList_fileName, 'r') #Read in the list of words to search for
    
    puzzle = getPuzzle(PUZZLE_FILE)
    wordList = getWordList(WORD_LIST) #Set our word list equal to variable
    
    print(wordList)
    printPuzzle(puzzle)
    
    for eachWord in wordList: # We call getFirstLetter() every time
        getFirstLetter(eachWord,puzzle)
    
    
    
    
    
    
    PUZZLE_FILE.close() #Close our files to save memory
    WORD_LIST.close() 
main()

