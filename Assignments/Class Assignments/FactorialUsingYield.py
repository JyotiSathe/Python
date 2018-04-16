#wap to accept a range from user and generate factorials of the given range

def Factorial(lb,ub):
    for i in xrange(lb,ub+1):
        fact=1
        for j in range(2,i+1):
            fact*=j
        yield fact

def main():
    lb=input("ENter Lower Bound")
    ub=input("ENter Upper Bound")
    n=Factorial(lb,ub)
    for i in xrange(lb,ub+1):
        print next(n)

if __name__=='__main__':
    main()
