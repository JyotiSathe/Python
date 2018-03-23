#WAP to validate am email id using regular expression
import re
def isValidEmailID(emailId):
    isValid=False
    if(not (type(re.search("([a-zA-Z0-9_\.]+)@([\w\.]+)\.([\w]+)",emailId))=='NoneType')):
        isValid=True
    return isValid

def main():
    emailId=input("Enter email ID:")
    if(isValidEmailID(emailId)):
        print("Valid")
    else:
        print("Not Valid")

if __name__=='__main__':
    main()
'''
>>> i=re.search("[a-zA-Z0-9]+@[a-z]+.com","jyotisathe1138@gmail.com")
>>> i.start(),i.end()
(0, 24)
'''
