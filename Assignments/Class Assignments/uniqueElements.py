#W a list comprehension to return unique element from a given list


def uniqueElements(list1):
    return [x for x in list1 if list1.count(x)==1]

def main():
    list1=[1,2,2,1,5,2,5,3,6]
    result=uniqueElements(list1)
    print result

if __name__=='__main__':
    main()
