#WAP to accept 2 numbers from user and print maximum out of them
def main():
    print("Enter 2 numbers:")
    num1=input("1st Number: ")
    num2=input("2nd Number: ")
    if(num1<num2):
        #max=num2
        print("%d is greater than %d"%(num2,num1))
    if(num2<num1):
        #max=num1
        print("%d is greater than %d"%(num1,num2))
    #print("Maximum of 2 numbers is ", max) --> output in () because it trates as tuple

def main2():
    print("main 2")
    print("Enter 2 numbers:")
    num1=input("1st Number: ")
    num2=input("2nd Number: ")
    if(num1<num2):
        print("%d is greater than %d"%(num2,num1))
    else:
        print("%d is greater than %d"%(num1,num2))
        
if __name__=='__main__':
    main()

