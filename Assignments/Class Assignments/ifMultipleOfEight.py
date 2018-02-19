#WAP to accept a number from user and check if it is multiple of 8 without using
# any arithmetic operator

def ifMultipleOfEight(n):
    flag=False
    if(n&7==0):
        flag=True
    return flag

def main():
    n=input("Enter a number")
    if(n>=8):
        if(ifMultipleOfEight(n)):
            print("%d is multiple of 8"%n)
        else:
            print("%d is not multiple of 8"%n)
    else:
        print("Enter number greater than 8")
    
if __name__=='__main__':
    main()
