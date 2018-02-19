#WAP to accept a file from user in below format and make a dictionary out of it
#and print it

def createDictUsingFile(filename):
    dict={}
    fd=open(filename)
    line=fd.readline()
    while line!="":
        lineStr=str(line)
        if lineStr.startswith("#") or lineStr.startswith("[") or lineStr.startswith("\n"):
            line=fd.readline()
            continue
        else:
            splitLine=lineStr.split("=")
            if(splitLine[1].contains("#")):
                splitLine[1]=splitLine[1].split("#")[0]
            if(splitLine[1].contains("\n")):
                splitLine[1]=splitLine[1].split("\n")[0]
            dict[splitLine[0]]=splitLine[1]
        line=fd.readline()
    return dict

def main():
    filename=input("Enter filename")
    output=createDictUsingFile(filename)
    print output
    

if __name__=='__main__':
    main()
