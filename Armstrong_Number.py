def isArmstrong(n):
    flag=False
    t=len(str(n))
    temp=n
    add=0
    while(n>0):
        r=n%10
        add+=r**t
        n=n/10
    if(add==temp):
        flag=True
    return flag

def main():
    n=input("Enter number to check if armstrong: ")
    flag=isArmstrong(n)
    if(flag):
        print("{} is Armstrong".format(n))
    else:
        print("{} is not Armstrong".format(n))
        
if __name__=='__main__':
    main()
