#WAP to check if number is 2s power or not without using arithemetic operators

def isRaiseToPower2(number):
    return (number&(number-1))==0

def main():
    number=input("Enter number to check if raise to power 2")
    isRaiseToPower2(number)

if __name__=='__main__':
    main()
