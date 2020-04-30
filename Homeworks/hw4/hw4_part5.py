#File:    hw4_part3.py                                                                                   
#Author:  Ati Ok                                                                                         
#Date:    February 24th, 2016                                                                            
#Section: 15                                                                                             
#Email:   ao10@umbc.edu                                                                                  
#Description: This file contains python code that prints numbers 1 to 100 per line with
#3 special cases where we print messages instead if a number meets certain requirements

def main():
    for x in range(1,101):
        if(x % 3 == 0 and x % 5 == 0): #this case goes first b/c it will appear for 
            print("In the future, everyone will be world famous for 15 minutes.")
        elif(x % 5 == 0):
            print("Where do you see yourself in five years?")
        elif(x % 3 == 0):
            print("Better three hours too son than a minute too late.")
        else:
            print(x)


main()
