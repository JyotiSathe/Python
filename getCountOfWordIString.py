#WAP to accept a string and a character or another string
#and without using count method count the occurences of second string in first
#
#Enter String"This is python program, it is getCountIfWordInString Assignment"
#Enter String to be checked if present in input string"is"
#'is' is present in 'This is python program, it is getCountIfWordInString Assignment' 3 times

def getCount(check_str,input_str):
    count=0
    for i in range(len(input_str)-len(check_str)+1):
        if(check_str==input_str[i:i+len(check_str)]):
            count=count+1
    return count

def main():
    input_str=input("Enter String")
    check_str=input("Enter String to be checked if present in input string")
    print("'{}' is present in '{}' {} times".format(check_str,input_str,getCount(check_str,input_str)))

if __name__=='__main__':
    main()
