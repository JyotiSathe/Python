#WAP to accept 2 numbers from user and print its GCD

def print_GCD(num1,num2):
    while num1!=num2:
        if num1>num2:
            num1=num1-num2
        else:
            num2=num2-num1
    return num1

def main():
    num1,num2=input("Enter 2 numbers")
    print("GCD of %d, %d is %d "%(num1,num2,print_GCD(num1,num2)))

if __name__=='__main__':
    main()
