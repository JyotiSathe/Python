#WAP to accept 3 numbers from user and print optimised minimum of them.
print("Enter 3 numbers:")
num1=input("1st Number: ")
num2=input("2nd Number: ")
num3=input("3rd Number: ")
min=num1
if(min>num2):
    min=num2
if(min>num3):
    min=num3
print("Minimum of 3 numbers is ", min)
