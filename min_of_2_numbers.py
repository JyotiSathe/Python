#WAP to accept 2 numbers from user and print minimum out of them
print("Enter 2 numbers:")
num1=input("1st Number: ")
num2=input("2nd Number: ")
if(num1>num2):
    min=num2
if(num2>num1):
    min=num1
print("Minimum of 2 numbers is ", min)
