#WAP to accept 3 numbers from user and print optimised max and min of them
def main():
    print("Enter 3 numbers:")
    num1=input("1st Number: ")
    num2=input("2nd Number: ")
    num3=input("3rd Number: ")
    max=num1
    if(max<num2):
        max=num2
    if(max<num3):
        max=num3
    print("Maximum of 3 numbers is ", max)

def brain():
    print("Enter 3 numbers:")
    num1=input("1st Number: ")
    num2=input("2nd Number: ")
    num3=input("3rd Number: ")
    if num1>num2 and num1>num3:
        print("%d is greater "%num1)
        #here num1 is rulled out
    elif num2>num3:
        print("%d is greater "%num2)
    else:
        print("%d is greater "%num3)

if __name__=='__main__':
    brain()
