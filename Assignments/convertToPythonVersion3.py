import re
def convertTo3Version(filename):
    fd=open(filename)
    
    fdw=open("F:/Python/temp.py","w")
    line=fd.readline()
    objPrint=re.compile("print ")
    objInput=re.compile("input")
    while line!="":
        matchPrint=objPrint.findall(line)
        matchInput=objInput.findall(line)
        if(matchPrint):
            line1=objPrint.sub("print (",line)
            line1=line1.replace(line1[-1],")",-1)
            fdw.write(line1+"\n")
        elif(matchInput):
            line1=objInput.sub("eval(input",line)
            line1=line1.replace(")","))")
            fdw.write(line1+"\n")
        else:
            fdw.write(line)
        line=fd.readline()

def main():
    filename=input("Enter File Name")
    convertTo3Version(filename)

if __name__=='__main__':
    main()
