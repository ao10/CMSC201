#File : hw3_part2.py
#Author: Ati Ok
#Date: February 21st, 2016
#Section: 15
#Email : ao10@Umbc.edu
#Description: This file contains python code that simulates a grading calculator

def main():
    hw_weight = float(input("Please enter the homework weight: "))
    hw_grade = int(input("Please enter the homework grade: "))
    exam_weight = float(input("Please enter the exam weight: "))
    exam_grade = int(input("Please enter the exam grade: "))
    disc_weight = float(input("Please enter the discussion weight: "))
    disc_grade = int(input("Please enter the discussion grade: "))
    weight_total = (hw_weight * hw_grade) + (exam_weight * exam_grade) + (disc_weight * disc_grade)
    
    if (weight_total >= 90):
        print("The final numerical grade is: ", weight_total)
        print("This earns you an A in the class.")
    
    elif (weight_total >=80 and weight_total <= 89.9):
        print("The final numerical grade is: ", weight_total)
        print("This earns you a B in the class.")
    
    elif (weight_total >= 70 and weight_total <= 79.9):
        print("The final numerical grade is: ", weight_total)
        print("This earns you a C in the class.")

    elif (weight_total >= 60 and weight_total <= 69.9):
        print("The final numerical grade is: ", weight_total)
        print("This earns you a D in the class.")
    
    elif (weight_total < 60):
        print("The final numerical grade is: ", weight_total)
        print("This earns you an F in the class.")





main()
