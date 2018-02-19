def getCount(n):
    count=0
    while(n!=0):
        print("in while")
        if(n&1==1):
            print("in if")
            count+=1
            print(count)
        print("out of if")
        n=n>>1
        print(n)
    return count

def main():
    n=input("Enter a number")
    print(getCount(n))

if __name__=='__main__':
    main()
