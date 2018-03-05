#WAP to implement complex number using Complex number


class Complex(object):
    def __init__(self,real=0,imag=0):
        self.real=real
        self.imag=imag

    def __add__(self,number):
        c1=Complex()
        if isinstance(number,complex):
            c1.real=self.real+number.real
            c1.imag=self.imag+number.imag
        elif isinstance(number,int):
            c1.real=self.real+number
            c1.imag=self.imag
        else:
            print("Invalid number")
        return c1
        '''if(type(number)==int):
            c1=self.real+number
        else:
            c1.real=self.real+number.real
            c1.imag=self.imag+number.imag'''

    def __repr__(self):
        return str(self.real)+str(self.imag)+"i"

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
            result=complexNum1+num
            print result.real+result.imag
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
