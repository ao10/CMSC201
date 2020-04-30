#File: hw6_part3.py
#Author: Ati Ok
#Date: 3/28/2016
#Section: 15
#Email: ao10@umbc.edu
#Description: This file contains python code that uses functions to draw a triangle, a square, 
#a paralellogram, or all three shapes as chosen by the user.

def drawTriangle(num): #This function takes in a positive integer entered in the main function and returns a triangle
    for x in range(1,num + 1): #we increment num by 1 because range is not inclusive at the 'stop' parameter
        print("*" * x) #we print out an asterisk for as big as x is # 1 star for 1 line, 2 stars for 2 lines, etc

def drawSquare(num): #This function takes in a positive integer entered in the main function and returns a square
    for x in range(1, num + 1):
        print(num * "*")    #an asterisk is printed 'num' times for 'num' lines 

def drawParalellogram(num): #This function takes in a positive integer entered in the main function and returns a triangle
    for x in range(1, num + 1):     #same as our drawSquare() function except we had to add 'x' number of spaces before 
        print(" " * x + num * "*") #we use string concatenation to add the number of spaces to the rest of the asterisks
                               
def main():
    num = int(input("Please enter a positive integer: "))
    while (num <= 0):
        num = int(input("Please enter a positive integer: "))
    
    shapeChoice = input("Please choose the shape: square, parellelogram, triangle, or all: ")
    while (shapeChoice != "square" and shapeChoice != "parellelogram" and shapeChoice != "triangle" and shapeChoice!= "all"):
        shapeChoice = input("Please choose the shape: square, parellelogram, triangle, or all: ")
        
    if (shapeChoice == "triangle"):
        drawTriangle(num)
    
    elif (shapeChoice == "square"):
        drawSquare(num)

    elif (shapeChoice == "paralellogram"):
        drawParalellogram(num)

    else:
        drawTriangle(num)
        print(" ")
        drawSquare(num)
        print(" ")
        drawParalellogram(num)



main()
