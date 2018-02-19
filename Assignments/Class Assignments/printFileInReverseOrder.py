#WAP to accept a file name from user and display file in reverse order without
#using loop, readlines(), without any built in container
#Hint:use recursive program

def reverseLineDisplay(fd):
    line=fd.readline()
    if(line==""):
        return
    reverseLineDisplay(fd)
    print line

def main():
    filename=input("Enter filename")
    fd=open(filename)
    reverseLineDisplay(fd)

if __name__=='__main__':
    main()
