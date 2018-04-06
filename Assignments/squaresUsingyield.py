def getSquares(lb,ub):
    for i in range(lb,ub+1):
        yield i*i

def main():
    lb=input("Enter Lower Bound")
    ub=input("Enter Upper Bound")
    n=getSquares(lb,ub)
    for i in range(lb,ub+1):
        print next(n)

if __name__=='__main__':
    main()
