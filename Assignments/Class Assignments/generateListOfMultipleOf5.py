#W a list comprehension to generate a list of multiples of 5

def generateListOfMultipleOf5(lb,ub):
    return [x for x in range(lb,ub) if(x%5==0)]

def main():
    lb,ub=input("Enter range")
    result=generateListOfMultipleOf5(lb,ub)
    print result

if __name__=='__main__':
    main()
