#WAP to check if a number entered is prime or notS
import math
def isPrime(num):
    if(num<0):
        num=num*-1
    if(num%2==0):
        return False
    for x in range(3,int(math.sqrt(num))+1,2):
        if(num%x==0):
            return False
    return True

def isPrime_1(num):
    flag=False
    if(num<0):
        num=num*-1
    if(num%2==0):
        flag=False
    for x in range(3,int(math.sqrt(num))+1,2):
        if(num%x==0):
            break
    else:
        flag=True
    return flag

def main():
    num=input("Enter number to check prime or not")
    if(isPrime_1(num)):
        print("%d is prime"%num)
    else:
        print("%d is not prime"%num)

if __name__=='__main__':
    main()
