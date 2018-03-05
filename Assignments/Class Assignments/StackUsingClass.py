#WAP program to implement a stack using class

class Stack:
    def __init__(self,size=10):
        self.STACK=[]
        self.size=size

    def __del__(self):
        del self_STACK
        print ("Destuctor")

    def isFull(self):
        return len(self.STACK)==self.size
    
    def isEmpty(self):
        return self.STACK==[]

    def Push(self,data):
        self.STACK.append(data)

    def Pop(self):
        self.STACK.pop()

    def display(self):
        print (self.STACK)

    def Menu(self):
        print ("1:Push")
        print ("2:Pop")
        print ("3:Display")
        print ("4:Exit")
        choice=input("Enter choice")
        return choice

def main():
    st1=Stack(5)
    choice=st1.Menu()
    while(choice<=3):
        if choice==1:
            if(not st1.isFull()):
                data=input("Enter Data")
                st1.Push(data)
            else:
                print ("Stack Full")
        elif choice==2:
            if(not st1.isEmpty()):
                st1.Pop()
            else:
                print ("Stack is Empty")
        elif choice==3:
            st1.display()
        else:
            print ("Invalid Choice")
        choice=st1.Menu()
            
if __name__=='__main__':
    main()
