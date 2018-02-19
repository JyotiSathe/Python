#WAP to accept a number from user and check if it is special number or not

def print_fact(n):
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    return fact

def isSpecialNumber(num):
    sum=0
    temp=num
    isSpecial=False
    while(num!=0):
        rem=num%10
        sum+=print_fact(rem)
        num=num/10
    if(temp==sum):
        isSpecial=True
    return isSpecial
        
def main():
    num=input("Enter number to check if special number or not")
    isSpecial=isSpecialNumber(num)
    if(isSpecial):
        print("{} is special number".format(num))
    else:
        print("{} is not special number".format(num))


if __name__=='__main__':
    main()
