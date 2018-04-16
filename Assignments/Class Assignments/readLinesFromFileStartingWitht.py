#WAP eo accept a filename from user and display all lines of the file which
#are starting with t/T

import re

def readLinesStartingWitht(filename):
    fd=open(filename)
    buf=fd.read()
    obj=re.compile("^t.*",re.I|re.M)
    for i in obj.findall(buf):
        print i

def main():
    filename=input("Enter Filename")
    readLinesStartingWitht(filename)

if __name__=='__main__':
    main()
