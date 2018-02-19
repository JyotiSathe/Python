#WAP to accept file from the user and print count of lines present in that file
#based on following filters:
#if filter comes as empty then line count
#if filter comes as "^Hello" then line count should be of lines which starts with Hello
#if filter comes as "Hello$" then line count should be of lines which ends with Hello
#if filter comes as "Hello" then line count where Hello in line


def countOfLinesWithFilterFromFile(filename,filter_str):
    fd=open(filename)
    line=fd.readline()
    count=0
    if(filter_str.startswith("^")):
        print("^")
        filter_str=filter_str[1:].lower()
        
        while(line!=""):
            input_str=str(line).lower()
            if(input_str.startswith(filter_str)):
                count+=1
            line=fd.readline()
    elif(filter_str.endswith("$")):
        print("$")
        filter_str=filter_str[0:-1].lower()
        while(line!=""):
            input_str=str(line).lower()
            if(input_str.strip().endswith(filter_str)):
                count+=1
            line=fd.readline()
    elif(not "^" in filter_str and not "$" in filter_str and filter_str!=""):
        print "here"
        while(line!=""):
            input_str=str(line).lower()
            if(filter_str.lower() in input_str):
                count+=1
            line=fd.readline()
    else:
        print("None")
        while(line!=""):
            count+=1
            line=fd.readline()
    return count

def Menu():
    print("1:^filter")
    print("2:filter$")
    print("3:filter in string")
    print("4:None")
    print("5:Exit")
    choice=input("Enter choice")
    return choice

def main():
    filename=input("Enter filename")
    choice=Menu()
    
    while(choice<5):
        if(choice==1):
            filter_str=input("Enter filter string")
            count=countOfLinesWithFilterFromFile(filename,"^"+filter_str)
            print(count)
        elif(choice==2):
            filter_str=input("Enter filter string")
            count=countOfLinesWithFilterFromFile(filename,filter_str+"$")
            print(count)
        elif(choice==3):
            filter_str=input("Enter filter string")
            count=countOfLinesWithFilterFromFile(filename,filter_str)
            print(count)
        elif(choice==4):
            count=countOfLinesWithFilterFromFile(filename,"")
            print(count)
        else:
            return
        choice=Menu()

if __name__=='__main__':
    main()
