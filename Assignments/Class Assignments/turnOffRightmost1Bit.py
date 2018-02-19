#WAP to accept a number from user and turn off its rightmost one bit

def turnOffRightmost1Bit(number):
    x=1
    while(number&x==0):
        x=x<<1
    return number&(~x)
    #return number^x
    '''while(True):
        if(number&x!=0):
            break
        x=x<<1
    return n&(~x)
    '''
    '''while(number!=0):
        count=1
        number=number>>1
        if(number&1==1):
            break
        count+=1
    print(count)'''

def main():
    number=input("Enter number")
    print(turnOffRightmost1Bit(number))

if __name__=='__main__':
    main()
