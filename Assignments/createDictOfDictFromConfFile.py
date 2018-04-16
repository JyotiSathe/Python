'''
    WAP to create a dictionary of dictionary from a file
    {General:{Master:True,SCORouting:PCM},
    Headset:{HFP:True,MaxConnected:1,FastConnectable:False}}
'''

def innerDict(fd):
    result={}
    line=fd.readline()
    while line !="" and not line.startswith("["):
        if not line.startswith("#"):
            if "=" in line:
                l1=line.split("=")
                value=l1[1]
                if "#" in value:
                    value=l1[1].split("#")[0]
                result[l1[0]]=value.rstrip()
        line=fd.readline()
    return line,result

def createDictOfDictFromConfFile(filename):
    fd=open(filename)
    outer={}
    inner={}
    line=fd.readline()
    while line!="":
        if line.startswith("["):
            print line
            key=line[1:line.index("]")]
            line,inner=innerDict(fd)
            outer[key]=inner
            continue
        line=fd.readline()
    return outer

def main():
    filename=input("Enter Configuration File Name")
    result=createDictOfDictFromConfFile(filename)
    print result

if __name__=='__main__':
    main()
