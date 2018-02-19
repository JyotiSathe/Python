#WAP to implement a stack using list

def isFull(l1):
    return len(l1)==10

def isEmpty(l1):
    return len(l1)==0

def push(l1,element):
    l1.append(element)

def pop(l1):
    l1.pop()
    
def Menu():
    print("1:Push\n2:Pop\n3:Print\n4:Exit")
    choice=input("Enter which operation to perform")
    return choice

def go_to_choice(choice,l1):
    if(choice==1):
        if(not isFull(l1)):
            element=input("Enter element")
            push(l1,element)
        else:
            print("Stack full")
    elif(choice==2):
        if(not isEmpty(l1)):
            pop(l1)
        else:
            print("Stack Empty")
    elif(choice==3):
        print l1
    else:
        return -1
            
def main():
    l1=[]
    choice=Menu()
    result=go_to_choice(choice,l1)
    while True:
        if(result==-1):
            break
        else:
            choice=Menu()
            result=go_to_choice(choice,l1)

if __name__=='__main__':
    main()
