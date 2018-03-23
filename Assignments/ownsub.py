

import re

def ownsub(string,replaceChar,replaceBy):
    replacedStr=""
    start=0
    end=0
    for i in re.finditer(replaceChar,string):
        end=i.start()      
        replacedStr+=string[start:end]
        replacedStr+=replaceBy
        start=i.end()
    return replacedStr

def main():
    string=input("Enter Sting: ")
    replaceChar=input("Enter What to replace: ")
    replaceBy=input("Enter replace By: ")
    replacedStr=ownsub(string,replaceChar,replaceBy)
    
    #replacedStr=ownsub("I am Good Good I am Good","Good","Bad")
    print(replacedStr)

if __name__=='__main__':
    main()

