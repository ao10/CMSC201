#File:    hw4_part3.py                                                                                   
#Author:  Ati Ok                                                                                         
#Date:    February 24th, 2016                                                                            
#Section: 15                                                                                             
#Email:   ao10@umbc.edu                                                                                  
#Description: This file contains python code that counts the number of times
#vowels appear in a string (a e i o u y)

def main():
    user_string = input("Please enter a string: ")
    numVowels = 0
    for x in user_string:
        if(x == 'a' or x == 'A' or x == 'e' or x =='E' or x == 'i' or x == 'I'): #check case
            numVowels += 1
        elif(x == 'o' or x == 'O' or x == 'u' or x == 'U' or x =='y' or x == 'Y'):
            numVowels += 1 #increment numVowels for every vowel we encounter
    print("There are",numVowels,"vowels in the string '",user_string,"'")



main()
