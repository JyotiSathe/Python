def returnMultipleOf64(lb,ub):
    for i in range(lb,ub+1):
        if(i&63==0):
            yield i

def main():
    lb=input("Enter Lower Bound")
    ub=input("Enter Upper Bound")
    n=returnMultipleOf64(lb,ub)
    for i in range(lb,ub+1):
        print next(n)

if __name__=='__main__':
    main()
