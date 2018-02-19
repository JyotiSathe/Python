#WAP to accapt file name and number of lines to be printed


def printLinesFromFile(filename,number_of_lines):
    fd=open(filename)
    line=fd.readline()
    count=1
    while(count<=number_of_lines):
        print line
        line=fd.readline()
        count+=1

def main():
    filename=input("Enter filename")
    number_of_lines=input("Enter number of lines")
    printLinesFromFile(filename,number_of_lines)

if __name__=='__main__':
    main()
