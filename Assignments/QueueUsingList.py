#WAP to implement queue using list

def isEmpty(l1):
    return len(l1)==0

def isFull(l1,MAXSIZE):
    return len(l1)==MAXSIZE

def Enqueue(l1):
    element=input("Enter element")
    l1.append(element)

def Dequeue(l1):
    l1.pop(0)

def go_to_choice(choice,l1,MAXSIZE):
    if(choice==1):
        if(not isFull(l1,MAXSIZE)):
           Enqueue(l1)
        else:
            print("Queue is full, no space for new elements!!!")
    elif(choice==2):
        if(not isEmpty(l1)):
            Dequeue(l1)
        else:
            print("Queue is already empty, please insert elements!!!")
    elif(choice==3):
        if(not isEmpty(l1)):
            print(l1)
        else:
            print("Queue is Empty, please insert elements!!!")
    else:
        return -1

def Menu():
    print("1:Enqueue\n2:Dequeue\n3:Print\n4:Exit")
    choice=input("Enter operation you want to perform")
    return choice

def main():
    l1=[]
    MAXSIZE=input("Enter number of elements in queue")
    choice=Menu()
    result=go_to_choice(choice,l1,MAXSIZE)
    while(result!=-1):
        choice=Menu()
        result=go_to_choice(choice,l1,MAXSIZE)

if __name__=='__main__':
    main()
