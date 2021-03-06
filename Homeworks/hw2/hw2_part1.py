#File:     hw2_part1.py
#Author:   Ati Ok
#Date:     February 8th, 2015
#Section:  15
#E-mail:   ao10@umbc.edu

def main():
#Question 1
#Expected output: 55
    question1 = (7+4) * 5
    print("Question 1 evaluates to: ", question1)
#Actual Output: 55
#Explanation: Parentheses first (11), then multiply by 5 (55)

#Question 2
#Expected output: 1
    question2 = 15 % 7
    print("Question 2 evaluates to: ", question2)
#Actual output: 1
#Explanation: 7 goes into 15 twice, leaving a remainder of 1

#Question 3
#Expected output: 32
    question3 = 32 % 36
    print("Question 3 evaluates to: ", question3)
#Actual output: 32
#Explanation: 36 does not go into 32; therefore there 32 remains

#Question 4 
#Expected output: 12
    question4 = (5 - 3) + (10 - 5) * (8 % 3)
    print("Question 4 evaluates to: ", question4)
#Actual output: 12
#Explanation: Parentheses evaluates to (2) + (5) * (2), then multiply (5*2) + 2 = 12  

#Question 5
#Expected output: 4.5
    question5 = 21 / 7 / 4 * (3 + 3)
    print("Question 5 evaluates to: ", question5)
#Actual output: 4.5
#Explanation: Parentheses first (6), evaluate left to right. 21 / 7 = 3 / 4 = 0.75 * 6 

#Question 6 
#Expected output: 14
    question6 = 9 / 3 + 21 - 5 * 2
    print("Question 6 evaluates to: ", question6)
#Actual output: 14.0
#Explanation: 9/3 gives us 3.0 add 21, (24) - (5*2), leaves us with 14.0.
# my mistake was that I did not add a decimal place because we had a floating point value.

#Question 7
#Expected output: 14
    question7 = 7 % 5 + 6 * 2
    print("Question 7 evaluates to: ", question7)
#Actual output 14
#Explanation: (7%5) leaves us with 2 + (6*2) is 14

#Question 8 
#Expected output: 34
    question8 = 35.2 / 2.3 + (332 % 33)
    print("Question 8 evaluates to: ", question8)
#Actual output: 17.30434782608696
#Explanation: 35.2 / 2.3 is evaluated first, then that is added to the remainder of (332%33)
# my mistake was that I got 34 as the remainder and forgot to add the quotient of 35.2 and 2.3

#Question 9
#Given equation : question9 = 55 / 10 + 45 / 0.2
#Solved equation : (55 / (10 + 45)) / 0.2
#Target number : 5.0
    question9 = (55 / (10 + 45)) / 0.2
    print("Question 9 evaluates to ", question9)

#Question 10
#Given equation : question10 = 65 // 20 + 10 - 4 % 4
#Solved equation : question10 = 65 // (20 + 10) - (4 % 4) 
#Target number : 2
    question10 = 65 // (20 + 10) - (4 % 4)
    print("Question 10 evaluates to ", question10)
main()



