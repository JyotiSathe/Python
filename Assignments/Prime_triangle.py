#WAP to accept number from user and print triangle of prime numbers
#2
#3 5
#7 11 13
#17 19 23 29
import math
def isPrime(num):
    if(num<0):
        num=num*-1
    if(num==2):
        return True
    if(num%2==0):
        return False
    for x in range(3,int(math.sqrt(num))+1,2):
        if(num%x==0):
            return False
    return True


def print_prime_triangle(rows):
    num=2
    for i in range(rows):
        for j in range(i+1):
            while(not isPrime(num)):
                num=num+1
            print num,
            num=num+1
        print

def main():
    rows=input("Enter number of rows")
    print_prime_triangle(rows)

if __name__=='__main__':
    main()
