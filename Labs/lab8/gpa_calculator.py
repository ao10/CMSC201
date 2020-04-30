#File: gpa_calculator.py
#Author: Ati Ok
#Date: April 4th, 2016
#Section: 15
#E-mail: ao10@umbc.edu

def convertLetter(letter):
    if (letter == "A"):
        return 4
    elif (letter == "B"):
        return 3
    elif (letter == "C"):
        return 2
    elif (letter == "D"):
        return 1
    else:
        return 0

def main():
    myInputFile = open("grades.txt", "r")
    myOutputFile = open("GPA.txt", "w")

    for line in myInputFile:
        line = line.strip()
        fname, lname, grade1, grade2, grade3 = line.split(";")
        myOutputFile.write(fname + ": " + str((convertLetter(grade1) + convertLetter(grade2) + convertLetter(grade3))/3) + "\n")
        
    myOutputFile = open("GPA.txt", "r")
    for line in myOutputFile:
        line = line.strip()
        print(line)


    myInputFile.close()
    myOutputFile.close()
main()
