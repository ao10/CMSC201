#tests whether myString is a palindrome
def isPalindrome(myString):
    tempString = myString
    length = len(tempString)
    half = length//2
    isPalindrome = True
    for i in range(0, half):
        if (tempString[i] != tempString[length-i-1]):
            isPalindrome = False
    print(isPalindrome)
#no errors below this line
def main():
    print("Should print: True\nPrints: ",end="")
    isPalindrome("oozyratinasanitaryzoo")
    print("Should print: False\nPrints:", end="")
    isPalindrome("18101181")
main()
