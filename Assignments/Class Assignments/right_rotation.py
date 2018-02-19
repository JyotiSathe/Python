#WAP to accept 2 substring from user and check if second string is right rotate of first
#eg.str1=India
#eg.str2=iaInd
def main():
    input_str1=input("Enter first string")
    input_str2=input("Enter second string")
    new_str=input_str1+input_str1
    if(len(input_str2)!=len(input_str1)):
        print("not right rotate")
    else:
        if(input_str2 in new_str):
            print("right rotate")
        else:
            print("not right rotate")

def isRotation(input_str,validate_str):
    if(len(input_str)==len(validate_str)):
        return validate_str in input_str+input_str
    return False

def main2():
    input_str1=input("Enter first string")
    input_str2=input("Enter second string")
    if isRotation(input_str1,input_str2):
        print("{} is rotation of {}".format(input_str2,input_str1))
        #one to one mapping
    else:
        print("{1} is not rotation of {0}".format(input_str1,input_str2))
if __name__=='__main__':
    main2()
