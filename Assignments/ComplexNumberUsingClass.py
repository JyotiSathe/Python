#WAP to implement complex number class

class Complex:
    def __init__(self,real=0,imag=0):
        self.real=real
        self.imag=imag
        self.num=real+imag

    def __del__(self):
        print ("Destructor")

    def addNumberToComplexNum(self,num):
        #return self.real+self.imag+num
        c=self
        return c.num+num

    def addTwoComplexNum(self,complexNum2):
        '''self.real+=complexNum2.real
        self.imag+=complexNum2.imag
        return self.real+self.imag'''
        c=self
        return c.num+complexNum2.num

    def subtractNumberToComplexNum(self,num):
        #return self.real+self.imag-num
        c=self
        return c.num-num

    def subtractTwoComplexNum(self,complexNum2):
        '''self.real-=complexNum2.real
        self.imag-=complexNum2.imag
        return self.real+self.imag'''
        c=self
        return c.num+complexNum2.num

def Menu():
    print ("1:Add number to complex number")
    print ("2:Add 2 Complex Numbers")
    print ("3:Subtract number from complex number")
    print ("4:Subtract 2 Complex numbers")
    choice=input("Enter which operation you want to perform")
    return choice

def main():
    choice=Menu()
    real1=input("Enter real part of a number")
    imag1=input("Enter imaginary part of a number")
    complexNum1=Complex(real1,imag1)
    while(choice<=5):
        if (choice==1):
            num=input("Enter number to add")
            print (complexNum1.addNumberToComplexNum(num))
        elif (choice==2):
            real2=input("Enter real part of second number")
            imag2=input("Enter imaginary part of second number")
            complexNum2=Complex(real2,imag2)
            print(complexNum1.addTwoComplexNum(complexNum2))
        elif (choice==3):
            num=input("Enter number to add")
            print (complexNum1.subtractNumberToComplexNum(num))
        elif (choice==4):
            real2=input("Enter real part of second number")
            imag2=input("Enter imaginary part of second number")
            complexNum2=Complex(real2,imag2)
            print(complexNum1.subtractTwoComplexNum(complexNum2))
        elif(choice==5):
            return
        else:
            print ("Enter valid choice")
            choice=Menu()
        choice=Menu()

if __name__=='__main__':
    main()
