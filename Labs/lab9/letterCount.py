#letterCount should take a letter and word,
#and count the number of times letter appears
#in the word
def letterCount(myLetter, myString):
    count = 0
    for i in myString:
        if (i == myLetter):
            count = count + 1
    print(count)
#no errors below this line
def main():
    print("Should print: 3\nPrints: ",end="")
    letterCount("a","aardvark")
main()
