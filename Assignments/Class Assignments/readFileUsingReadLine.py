#WAP to accept file name from user and print it line by line using readline

def readFile(filename):
    fd=open(filename)
    line=fd.readline()
    while line!="":
        print line
        line=fd.readline()

def main():
    filename=input("Enter file name")
    readFile(filename)

if __name__=='__main__':
    main()
