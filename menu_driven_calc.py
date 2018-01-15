#WAP to perform menu driven arithmetic operations
import sys
def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
        return n1/n2

def rem(n1,n2):
    return n1%n2

def get_choice():
    print("***MENU***")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Modulus")
    print("6: Exit")
    choice=input("Enter your choice\n")
    return choice

def perform(choice):
    n1,n2=input("Enter 2 numbers")
    if(choice==1 or choice=="Addition"):
        print("Addition of {} + {} is {}".format(n1,n2,add(n1,n2)))
    elif(choice==2 or choice=="Subtraction"):
        print("Subtraction of {} - {} is {}".format(n1,n2,sub(n1,n2)))
    elif(choice==3 or choice=="Multiplication"):
        print("Multiplication of {} * {} is {}".format(n1,n2,mul(n1,n2)))
    elif(choice==4 or choice=="Division"):
        if(n2==0):
            print("Dividend cannot be zero")
        else:
            print("Division of {} / {} is {}".format(n1,n2,div(n1,n2)))
    elif(choice==5 or choice=="Modulus"):
        print("Remainder of {} % {} is {}".format(n1,n2,rem(n1,n2)))
    else:
        sys.exit
        #return

def main():
    choice=get_choice()
    if(not (choice>=6) and not(choice=="Exit")):
        perform(choice)

if __name__=='__main__':
    main()
