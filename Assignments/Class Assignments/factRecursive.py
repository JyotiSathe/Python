#WAP to accept a number from user and print a factorial using recursion method
def factRecursive(num):
    if(num==0):
        return 1
    return num*factRecursive(num-1)

def main():
    n=input("Enter number")
    print("Factorial of {} is {}".format(n, factRecursive(n)))

if __name__=='__main__':
    main()
