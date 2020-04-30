#File: proj1.py
#Author: Ati Ok
#Date: April 10th, 2016
#Section: 15
#E-mail: Ao10@umbc.edu
#Description: This file contains python code that simulates a game of tic-tac-toe
#You are able to save and load games as well, and you can play with 2 players
import random
NUM_TURNS_P1 = 5
NUM_TURNS_P2 = 4
P1_TURN = True
P2_TURN = False
def printBoard(grid): #This function takes in the list of integers and prints it out as a 3x3 TTT board
    for i in range(len(grid)//3):  #Print the first 3 elements
        print(grid[i] , end = ' ')
    print(end = "\n")
    for i in range(len(grid)//3):  #Print the next 3
        print(grid[i+3] , end = ' ')
    print(end = "\n")
    for i in range(len(grid)//3):  #Print the last 3
        print(grid[i+6] , end = ' ')
    print(end = "\n")


def createGrid(): #Creates and returns a pre-determined initialized list that represents our TTT board
    grid = [1,2,3,4,5,6,7,8,9]
        #  [0,1,2,3,4,5,6,7,8]
    return grid

def getPlayer(): #Generates and returns a random number between 1 and 2 decides which player goes first
    player = random.randint(1,2)
    if (player == 1): #Player 1 goes first
        return 1
    else:             #Player 2 goes first
        return 2

def getSymbol(): #Generates a random number between 1 and 2 and returns either 'X' or 'O'
    symbol = random.randint(1,2)
    if (symbol == 1):
        return 'X'
    else:
        return 'O'
    
def fillIn(grid, choice, symbol): #This function takes in 2 parameters (a grid, and the user's choice to fill in on the grid), then the function returns the new grid with a change in the TTT-board
    newGrid = grid[:]
    for i in range(len(newGrid)):
        if (newGrid[i] == choice):
            newGrid[i] = (symbol)
    #print(newGrid)
    return newGrid

def saveGame(grid): #This function saves the current board if the user enters -1
                    #it writes the board to a static filed called "tic.txt"
    myFile = open("tic.txt", "w")
    for i in range(len(grid)):
        myFile.write(str(grid[i]) + "\n") #DONT FORGET TO CAST THESE BACK TO INTEGERS WHEN YOU LOAD
                                   #WE CASTED THESE AS STRINGS BECAUSE WE CAN'T WRITE INTEGERS TO FILES
    print("File saved.")
    myFile = open("tic.txt", "r")
    print("Here is what saved: ")
    myFile.close()
    
def loadGame(): #This is a void function that returns the grid, the current user's turn, and the current user's symbol
    myFile = open("tic.txt")
    grid = []
    for eachLine in myFile:
        eachLine.strip()
        grid.append(eachLine[0])
    print("This is the grid from the loaded file! ")
    print(grid)
    
    
    
    return grid #grid is a list of 9 integers/strings that represent our tic-tac-toe board
    myFile.close()

def checkP1Win(grid, firstSymbol): #Takes in the first mover's symbol and current board as parameter
    #Possible winning scenarios:
    # 1 | 1 | 1    _ | _ | _   _ | _ | _   4 | _ | _   _ | 5 | _   _ | _ | 6 
    # _ | _ | _    2 | 2 | 2   _ | _ | _   4 | _ | _   _ | 5 | _   _ | _ | 6
    # _ | _ | _    _ | _ | _   3 | 3 | 3   4 | _ | _   _ | 5 | _   _ | _ | 6

    # 7 | _ | _    _ | _ | 8   0 | 1 | 2 
    # _ | 7 | _    _ | 8 | _   3 | 4 | 5
    # _ | _ | 7    8 | _ | _   6 | 7 | 8
    if (grid[0] == firstSymbol and grid[1] == firstSymbol and grid[2] == firstSymbol):
        print("Player 1 wins!")
        return True
    elif (grid[3] == firstSymbol and grid[4] == firstSymbol and grid[5] == firstSymbol):
        print("Player 1 wins!")
        return True
    elif (grid[6] == firstSymbol and grid[7] == firstSymbol and grid[8] == firstSymbol):
        print("Player 1 wins!")
        return True
    elif (grid[0] == firstSymbol and grid[3] == firstSymbol and grid[6] == firstSymbol):
        print("Player 1 wins!")
        return True
    elif (grid[1] == firstSymbol and grid[4] == firstSymbol and grid[7] == firstSymbol):
        print("Player 1 wins!")
        return True
    elif (grid[2] == firstSymbol and grid[5] == firstSymbol and grid[8] == firstSymbol):
        print("Player 1 wins!")
        return True
    elif (grid[0] == firstSymbol and grid[4] == firstSymbol and grid[8] == firstSymbol):
        print("Player 1 wins!")
        return True
    elif (grid[2] == firstSymbol and grid[4] == firstSymbol and grid[6] == firstSymbol):
        print("Player 1 wins!")
        return True
    else:
        return False

def checkP2Win(grid, secondSymbol):
    if (grid[0] == secondSymbol and grid[1] == secondSymbol and grid[2] == secondSymbol):
        print("Player 2 wins!")
        return True
    elif (grid[3] == secondSymbol and grid[4] == secondSymbol and grid[5] == secondSymbol):
        print("Player 2 wins!")
        return True
    elif (grid[6] == secondSymbol and grid[7] == secondSymbol and grid[8] == secondSymbol):
        print("Player 2 wins!")
        return True
    elif (grid[0] == secondSymbol and grid[3] == secondSymbol and grid[6] == secondSymbol):
        print("Player 2 wins!")
        return True
    elif (grid[1] == secondSymbol and grid[4] == secondSymbol and grid[7] == secondSymbol):
        print("Player 2 wins!")
        return True
    elif (grid[2] == secondSymbol and grid[5] == secondSymbol and grid[8] == secondSymbol):
        print("Player 2 wins!")
        return True
    elif (grid[0] == secondSymbol and grid[4] == secondSymbol and grid[8] == secondSymbol):
        print("Player 2 wins!")
        return True
    elif (grid[2] == secondSymbol and grid[4] == secondSymbol and grid[6] == secondSymbol):
        print("Player 2 wins!")
        return True
    else:
        return False



def main():
    num_turns_p1 = 5
    num_turns_p2 = 4
    P1_TURN = True
    P2_TURN = False
    P1_WIN = False
    P2_WIN = False
    print("Welcome to Tic-Tac-Toe!")
    print("This is for two players!")
    
    firstMover = str(getPlayer()) #Call the functions to initialize our players and symbols
    firstSymbol = getSymbol() #See who goes first
    
    if (firstMover == '1'): #Set the 2nd player with the other player number (either 1 or 2)
        secondMover = str(2)
    else:
        secondMover = str(1)
        
    if (firstSymbol == 'X'):  #Set the 2nd player with the other symbol (either 'X' or 'O')
        secondSymbol = "O"
    else:
        secondSymbol = "X"
        
    print("Player " + firstMover + " will go first and will play with the " + (firstSymbol))
        
    grid = createGrid() #We call this function to make a 3x3 tic-tac-toe board
    printBoard(grid)
    print("\n")
    userChoice = 0
    newBoard = grid[:]
    while (P1_WIN == False and P2_WIN == False):
            
        while(num_turns_p1 > 0 and P1_TURN == True and (P1_WIN == False and P2_WIN == False) and userChoice != -1):
            print("Player " + firstMover + " what is your choice? ")
            userChoice = int(input("(1-9) or -1 to save or -2 to load: "))
            while (userChoice != -1 and userChoice != -2) and (userChoice < 1 or userChoice > 9):
                print("Player " + firstMover + " what is your choice? ")
                userChoice = int(input("(1-9) or -1 to save or -2 to load: "))
            if (userChoice == -1):
                saveGame(newBoard)   #FIX ME
            elif (userChoice == -2):
                newBoard = loadGame()
                newBoard = fillIn(newBoard,userChoice,firstSymbol)

                #Whatever board was saved gets opened up
            elif (userChoice >= 1 and userChoice <= 9):
                newBoard = fillIn(newBoard,userChoice,firstSymbol)
            P1_TURN = False
            num_turns_p1 -= 1
            P2_TURN = True
            if (checkP1Win(newBoard, firstSymbol) == True):
                P1_WIN = True
            elif (checkP2Win(newBoard, secondSymbol) == True):
                P2_WIN = True
            printBoard(newBoard)
            #if numTurns_P1 reches 0 then tell them its a draw
    
        while(num_turns_p2 > 0 and P2_TURN == True and (P2_WIN == False and P1_WIN == False) and userChoice != -1):
            print("Player " + secondMover + " what is your choice? ")
            userChoice = int(input("(1-9) or -1 to save or -2 to load: "))
            while (userChoice != -1 and userChoice != -2) and (userChoice < 1 or userChoice > 9):
                print("Player " + secondMover + " what is your choice? ")
                userChoice = int(input("(1-9) or -1 to save or -2 to load: "))
            if (userChoice == -1):                      
                saveGame(newBoard)                                                           
            elif (userChoice == -2):                      
                newBoard = loadGame()
                newBoard = fillIn(newBoard,userChoice,firstSymbol)
                #Whatever board was saved gets opened up  
            elif (userChoice >= 1 and userChoice <= 9):
                newBoard = fillIn(newBoard,userChoice, secondSymbol)
            P2_TURN = False
            num_turns_p2 -= 1
            P1_TURN = True
            if (checkP2Win(newBoard, secondSymbol) == True):
                P2_WIN = True
            elif (checkP1Win(newBoard, firstSymbol) == True):
                P1_WIN = True
            printBoard(newBoard)
            #if numTurns_P2 reaches 0 then tell them its a draw
        if (userChoice == -1):
            userChoice = input("Play again? ")
            while (userChoice == 'yes'):
                    #Run the game again
                    main()
                    
        if (num_turns_p1 - 1 == 0 and num_turns_p2 == 0):
            print("Draw!")
            userChoice = input("Play again? ")
            userChoice = userChoice.lower()
            while (userChoice == 'yes' or userChoice == 'y' or userChoice):
                    #Run the game again
                    if(userChoice == 'yes' or userChoice =='y'):
                        main()
                    elif(userChoice == 'no' or userChoice =='n'):
                        print("Thanks for playing!")
                        userChoice = "" #Set userChoice to null so it doesnt give us an infinite loop
                    
main()

