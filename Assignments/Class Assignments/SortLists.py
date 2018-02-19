#WAP to accept 2 list from user ,sort them without using built in sort method
#and then merge the 2 sorted list

def sortlist(l1):
    #templist=[]
    for i in range(len(l1)):
        for j in range(i):
            if(l1[j]>l1[j+1]):
                temp=l1[j+1]
                l1[j+1]=l1[j]
                l1[j]=temp
                print l1
    print l1

def merge(l1,l2):
    i=0
    j=0
    l3=[]
    while(i<len(l1) and j<len(l2)):
        if(l1[i]<l2[j]):
            l3.append(l1[i])
            i+=1
        else:
            l3.append(l2[j])
            j+=1
    if(i<len(l1)):
        l3.extend(l1[i:])
    if(j<len(l2)):
        l3.extend(l2[j:])
    return l3

def sortedlist(l1):
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if(l1[i]>l1[j]):
                temp=l1[j]
                l1[j]=l1[i]
                l1[i]=temp
    return l1

def main():
    l1=sortedlist(input("Enter list:"))
    print l1
    l2=sortedlist(input("Enter list:"))
    print l2
    mergedList=merge(l1,l2)
    print(mergedList)

if __name__=='__main__':
    main()
