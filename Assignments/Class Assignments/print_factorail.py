#WAP to accept a number from user and print its factorial
def print_fact(n):
    fact=1
    for i in range(2,n+1):
        fact*=i
    return fact

def Factorial(number):
    fact=-1
    if number>0:
        if number<3:
            fact=number
        else:
            fact=1
            while number!=1:
                fact*=number
                number-=1
    return fact
    
def main():
    n=input("Enter number")
    print("Factorial of {} is {}".format(n, Factorial(n)))

if __name__=='__main__':
    main()
