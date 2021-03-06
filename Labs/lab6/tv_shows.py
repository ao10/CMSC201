#File: tv_shows.py
#Author: Ati Ok
#Date: Monday, March 21st
#Section: 15
#E-mail: ao10@umbc.edu


def main():
    shows = ["Daredevil", "Fargo", "Limitless", "Elementary", "Brooklyn 99", "Empire", "Supergirl"]
    for i in range(len(shows)):
        print(i + 1, " - " , shows[i])
    
    showVotes = [0, 0, 0, 0, 0, 0, 0,] #list of 7 
    vote = -1
    print("Which show would you like to vote for? ")
    while (vote != 0):
        vote = int(input("Enter '0' to stop voting: "))
        if (vote > 0 and vote < 8):  #Shows 1 through 7
            showVotes[vote - 1] = showVotes[vote - 1] + 1 #increment by 1 

    print("Here are the final votes: ")
    for i in range(len(shows)):
        print(shows[i], "has: ", showVotes[i], "votes")
            


main()
