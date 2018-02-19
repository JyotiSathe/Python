#WA list comprehension to geneate tables for the given range

def returnTables(lb,ub):
    return [x*i for x in range(lb,ub+1) for i in range(1,10+1)]

def main():
    lb,ub=input("Enter range")
    result=returnTables(lb,ub)
    print result

if __name__=='__main__':
    main()
