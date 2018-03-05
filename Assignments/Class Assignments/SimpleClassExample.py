#WAP to create a class

class SimpleClass:
    #class attribute
    institute_name="Trinaha Solutions" 
    def __init__(self,value):
        #object attribute which is present for object
        self.__private_attribute=100
        self.object_attribute=value 
        print("Constructor")
        
    def __del__(self):
        print("Destructor")

    def setAttribute(self,value):
        self.object_attribute=value

    def __setPrivateAttribute(self,value):
        print("in private setter")
        self.__private_attribute=value

    def getAttribute(self):
        print id(self)
        return self.object_attribute
    
def main():
    x=SimpleClass(10)
    y=SimpleClass(20)
    #print id(x)
    print x.object_attribute
    #print (x.getAttribute())
    #print id(y)
    print y.object_attribute
    #print (y.getAttribute())
    x.teach=True
    print x.__dict__
    print y.__dict__
    #print SimpleClass.__dict__
    #print SimpleClass.institute_name
    print x._SimpleClass__private_attribute
    
    x._SimpleClass__setPrivateAttribute(1000)
    print x._SimpleClass__private_attribute
    print x.__dict__
    print y.__dict__

if __name__=='__main__':
    main()
