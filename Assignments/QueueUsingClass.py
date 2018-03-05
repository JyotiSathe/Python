#WAP to implement Queue using class

class Queue:

    def __init__(self,size=10):
        self.QUEUE=[]
        self.size=size
        print ("Contructor")

    def __del__(self):
        del self_QUEUE
        print("Destructor")

    def isFull(self):
        return len(self.QUEUE)==self.size

    def isEmpty(self):
        return self.QUEUE==[]

    def insert(self,data):
        self.QUEUE.append(data)    

    def delete(self):
        self.QUEUE.pop(0)
        
    def display(self):
        print (self.QUEUE)
        
    def Menu(self):
        print ("1:Insert")
        print ("2:Delete")
        print ("3:Display")
        print ("4:Exit")
        choice=input("Enter choice")
        return choice

def main():
    qu1=Queue(5)
    choice=qu1.Menu()
    while(choice<=3):
        if choice==1:
            if(not qu1.isFull()):
                data=input("Enter Data")
                qu1.insert(data)
            else:
                print ("Queue Full")
        elif choice==2:
            if(not qu1.isEmpty()):
                qu1.delete()
            else:
                print ("Queue is Empty")
        elif choice==3:
            qu1.display()
        else:
            print ("Invalid Choice")
        choice=qu1.Menu()

if __name__=='__main__':
    main()
