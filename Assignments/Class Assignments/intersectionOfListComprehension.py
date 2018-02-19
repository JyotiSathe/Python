#WA list comprehension which returns intersection of 2 list

def intersectionOfList(l1,l2):
    #return [x for x in l1 for i in l2 if(x==i)]
    return [x for x in l1 if x in l2]

def main():
    l1=[1,3,46,78,9,25]
    l2=[2,3,78,90,10,30,25]
    result=intersectionOfList(l1,l2)
    print result

if __name__=='__main__':
    main()
