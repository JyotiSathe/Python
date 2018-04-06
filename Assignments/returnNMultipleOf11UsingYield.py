def returnMultipleOf11(n):
    for i in range(1,n+1):
        yield 11*i

def main():
    n=input("Enter how many multiples")
    num=returnMultipleOf11(n)
    for i in range(1,n+1):
        print next(num)


if __name__=='__main__':
    main()
