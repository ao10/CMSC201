#File: hw5_part4.py
#Author: Ati Ok
#Date: Sunday, March 6th, 2016
#Section: 15
#Email: ao10@umbc.edu
#Description: This program simulates an extra credit game using nested while loops and input validation

def main():
    challengePoints = int(input("Enter the number of points to play for (13-21): "))

    while (challengePoints < 13 or challengePoints > 21): #Let this run until user enters valid value between 13 and 21
        print("Error: You can play for 13-21 points")
        challengePoints = int(input("Enter the number of points to play for (13-21): "))
    print("Player 2 starts.")
    while (challengePoints > 0): #It will keep prompting to take points if it is greater than 0 
        print("There are",challengePoints,"left.")
        numTakes = int(input("Player 2, how many points do you take? (1-3): "))

        if (challengePoints == 2 and numTakes >= 3): #This switch statement activates if there is only 2 points remaining
            print("Error: You can take 1-2 points")  #it will tell the user you can only take 1-2 points, and not 3
            numTakes = int(input(("Player 2, how many points do you take? (1-2): ")))

        while(numTakes < 1 or numTakes > 3): #Input validation if user enters more than 3 or less than 1 point(s)
            print("Error: You can take 1-3 points")
            numTakes = int(input("Player 2, how many points do you take? (1-3): "))
        challengePoints -= numTakes
        if (challengePoints == 0):
            print("Congratulations! Player 2 has won!!!")
    


main()
