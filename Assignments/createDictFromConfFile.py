'''
    Write a program to accept a file name from user which contains data in following format. Create a dictionary out of this format.
    audio = True
    HFP = False
    Gateway = True

    Handle below scenarios:
    --
    audio = True #audio config
    gateway=false
    [SBC]
    Anything other then the pairs should be removed. All such cases should be ignored.
'''

def createDictFromConfFile(filename):
    fd=open(filename)
    line=fd.readline()
    dict1={}
    while line!="":
        if not line.startswith("#"):
            if "=" in line:
                l1=line.split("=")
                value=l1[1]
                if "#" in value:
                    value=l1[1].split("#")[0]
                dict1[l1[0]]=value.rstrip()
        line=fd.readline()
    return dict1

def main():
    filename=input("Enter COnfiguration File Name")
    result=createDictFromConfFile(filename)
    print result

if __name__=='__main__':
    main()
