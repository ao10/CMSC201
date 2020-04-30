#Ati Ok

def getDictionary(myFile): #Takes in a file name and returns a dictionary

    stateDict ={}

    for eachLine in myFile:
        state = eachLine.strip().split(',') #This splits each line as ['Maryland', 'MD']
        stateDict[state[0]] = state[1]
    return stateDict

def main():
    #State names are the key, abbreviation is the value
    #(i.e. 'Maryland' : MD)
    myFile = open("states.txt")
    stateDictionary = getDictionary(myFile)
    stateInput = ' '
    print(stateDictionary)
    while (stateInput != 'exit'):
        stateInput = input("Please enter a state to abbreviate (list to get list and exit to exit): ")
        if (stateInput in stateDictionary == False):
            print("Sorry. That is not in the dictionary.")
        elif (stateInput != 'exit'):
            print("The abbreviation of the state " + stateInput + " is "+ stateDictionary[stateInput])


    myFile.close()
main()
