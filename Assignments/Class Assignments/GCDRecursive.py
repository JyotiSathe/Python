#WAP to accept 2 numbers from user and print its GCD using recursion

def GCDRecursive(num1,num2):
    if num1==num2:
        return num1
    if num1>num2:
        num1-=num2
    else:
        num2-=num1
    return GCDRecursive(num1,num2)
    
def main():
    num1,num2=input("Enter 2 numbers")
    print("GCD of %d, %d is %d "%(num1,num2,GCDRecursive(num1,num2)))

if __name__=='__main__':
    main()
