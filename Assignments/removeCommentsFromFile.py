#WAP to accept a filename from user and remove all single and multi line comments from that file
'''read a file
#
'''
'''
import tempfile
write lines withuot comment to temp file 
copy content of temp file into original file
'''
import tempfile
import re
import os
def removeCommentsFromFile(filename):
    fd=open(filename)
    line=fd.readline()
    fdw=open("F:/Python/commented.txt","w")
    fdtemp=open("F:/Python/uncommented.txt","w")
    obj=re.compile("^#\w+")
    obj2=re.compile("^'''\w*")
    while(line!=""):
        if(obj.findall(line)):
            print "in if"
            fdw.write(line)
        elif(obj2.findall(line)):
            print "in elif"
            line2=fd.readline()
            while(not obj2.findall(line2)):
                fdw.write(line2)
                line2=fd.readline()
        else:
            fdtemp.write(line)
        print "here"
        line=fd.readline()
    fd.close()
    #fdw.close()
    fdtemp.close()
    fdtemp=open("F:/Python/uncommented.txt","r")
    fd=open(filename,"w")
    line=fdtemp.readline()
    while(line!=""):
        fd.write(line)
        line=fdtemp.readline()
    fd.close()
    fdtemp.close()
    os.remove("F:/Python/uncommented.txt")

def main():
    filename=input("Enter Filename")
    removeCommentsFromFile(filename)

if __name__=='__main__':
    main()
