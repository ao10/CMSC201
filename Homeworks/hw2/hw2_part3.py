#File : hw2_part3.py
#Author : Ati Ok
#Date : February 14th, 2016
#Email : ao10@umbc.edu
#Section : 15 

def main():
    price = float((input("What is the price? ")))
    dollar = int(price)
    cents = price - dollar
    print("The number of dollars is : ", dollar)
    print("The number of cents is : ", cents)


main()
