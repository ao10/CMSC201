#File:    hw4_part3.py
#Author:  Ati Ok                                                                                         
#Date:    February 24th, 2016                                                                            
#Section: 15                                                                                             
#Email:   ao10@umbc.edu                                                                                  
#Description: This file contains python code that measures the amount of donations 
#from a polar bear plunge

def main():
    pledges = int(input("How many pledges did you get?"))
    donations = 0
    for n in range(1, pledges + 1): #asks for donations starting at #1
        donations += float(input("What is the value of donation "+ str(n) + ":")) 

    numPlunges = int(input("How many plunges did you do?"))
    total = float(donations * numPlunges)

    print("Based on your",numPlunges,"plunges you earned $",str(total), "for the charity")


main()
