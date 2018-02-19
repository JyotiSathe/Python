#WAP to accept name of file from user and display longest and smallest line from it


def findLongSmallLine(filename):
    fd=open(filename)
    line=fd.readline()
    input_str=str(line)
    longest_line=input_str
    smallest_line=input_str
    longest_length=len(input_str)
    smallest_length=len(input_str)
    while line!="":
        if(longest_length<len(str(line))):
            longest_line=str(line)
            longest_length=len(input_str)
        if(smallest_length>len(str(line))):
            smallest_line=str(line)
            smallest_length=len(input_str)
        line=fd.readline()

    return longest_line,smallest_line

def main():
    filename=input("Enter filename from which to find longest and smallest line")
    longest_line,smallest_line=findLongSmallLine(filename)
    print("Longest line is {} ".format(longest_line))
    print("Smallest line is {} ".format(smallest_line))

if __name__=='__main__':
    main()
