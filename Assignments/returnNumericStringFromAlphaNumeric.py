#WAP to accept an alphanumeric string from user and remove all characters
#other than digits using re
import re
def removeCharacters(alphanumericStr):
    return re.sub("[a-zA-Z]","",alphanumericStr)

def main():
    alphanumericStr=input("Enter String: ")
    numericString=removeCharacters(alphanumericStr)
    print(numericString)

if __name__=='__main__':
    main()
