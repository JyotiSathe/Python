#WAP to accept a number from user and check if it is multiple of 32 without using
# any arithmetic operator

def ifMultipleOfThirtyTwo(n):
    return n&31==0

def main():
    n=input("Enter a number")
    if(n>=32):
        if(ifMultipleOfThirtyTwo(n)):
            print("%d is multiple of 32"%n)
        else:
            print("%d is not multiple of 32"%n)
    else:
        print("Enter number greater than 32")
    
if __name__=='__main__':
    main()
