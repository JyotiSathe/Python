#WAP to accept filename from user and display all words which are starting
#with digit or an underscore, print words

import re

def wordsStartingWithDigit_(filename):
    fd=open(filename)
    line=fd.readline()
    obj=re.compile(r"\b[0-9_]\w+",re.M)
    while(line!=""):
        for i in obj.findall(line):
            print i
        line=fd.readline()

def main():
    filename=input("Enter filename")
    wordsStartingWithDigit_(filename)

if __name__=='__main__':
    main()
