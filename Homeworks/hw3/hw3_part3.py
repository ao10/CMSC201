#File : hw3_part3.py
#Date : February 22, 2016
#Author: Ati Ok
#Section: 15
#Email: ao10@umbc.edu
#Description: This file simulates a "Guess Who" - like game

def main():
    print("Please enter 'y' for yes and 'n' for no to these questions.")

    ans = input("Is your character a woman? (y/n): ")
    if (ans == 'y'):
        blue_eyes = input("Does your character have blue eyes? (y/n): ")
        if (blue_eyes == 'y'):
            print("Your character is Jane!")
        elif (blue_eyes == 'n'):
            print("Your character is Marni!")
    
    if (ans == 'n'):
        glasses = input("Does your character wear glasses? (y/n): ")
        if (glasses == 'y'):
            print("Your character is Adrian!")
        elif (glasses == 'n'):
            beard = input("Does your character have a beard? (y/n): ")
            if (beard == 'y'):
                print("Your character is Peder!")
            elif (beard == 'n'):
                print("Your character is Zhang!")



main()
