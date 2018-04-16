#WAP to accept a name of file and the pattern to be searched at beginning.
#Write a generator which returns the lines matching the given pattern

import re

def linesWithPattern(filename,pattern):
    fd=open(filename)
    pattern="^"+pattern
    obj=re.compile(pattern)
    line=fd.readline()
    while line!="":
        if obj.findall(line):
            yield line
        line=fd.readline()

def main():
    filename=input("Enter Filename")
    pattern=input("Enter Pattern To Be Searched At the Beginning")
    line=linesWithPattern(filename,pattern)
    while True:
        print next(line)

if __name__=='__main__':
    main()
