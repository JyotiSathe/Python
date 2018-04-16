def FibonacciSeries(lb,ub):
    x=1
    y=1
    next=2
    while next<ub:
        if next>=lb:
            yield next
        next=x+y
        x=y
        y=next
    

def main():
    lb=input("Enter Lower Bound")
    ub=input("Enter Upper Bound")
    l1=FibonacciSeries(lb,ub+1)
    for i in l1:
        print i
    #for i in xrange(lb,ub):
    #    print next(l1)

if __name__=='__main__':
    main()
