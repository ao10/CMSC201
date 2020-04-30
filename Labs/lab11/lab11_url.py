import urllib.request

def main():
    #Step 1: add function from urllib.request
    #  Open http://www.cnn.com
    mySite = urllib.request.urlopen('http://www.cnn.com')

    #Step 2: Read in the webpage as a string
    mySiteString = mySite.read()
    
    #Step 3: Print the string and 
    #print the length of the webpage
    print(mySiteString)
    print(len(mySiteString))
main()
