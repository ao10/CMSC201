#File:    hw4_part2.py                                                                                  
#Author:  Ati Ok                                                                                         
#Date:    February 24th, 2016                                                                            
#Section: 15                                                                                             
#Email:   ao10@umbc.edu                                                                                  
#Description: This file contains python code that outputs every third letter from 
#a string given to you by the user

def main():
    string = input("Please enter a sentence: ")
    for x in range(0,len(string),3):
        print(string[x], end = "") #This removes the space and prints on one line dynamically

main()          
