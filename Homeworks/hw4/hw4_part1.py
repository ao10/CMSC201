#File:    hw4_part1.py
#Author:  Ati Ok
#Date:    February 24th, 2016
#Section: 15 
#Email:   ao10@umbc.edu
#Description: This file contains pyhton code that demonstrates for loops 
#used to create a multiplation table.

def main():
    base_num = int(input("Enter the base number: "))
    max_num = int(input("Enter the max number: "))
    for i in range(max_num + 1): #this loop runs base_num times
        print(str(base_num)+"*"+str(i)+"="+str(base_num*i)) #multiply i by base_num each time
#i increases by 1 each iteration
        


main()
