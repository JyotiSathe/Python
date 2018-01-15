#WAP to accept a number from user and check if it is paindrome or not
def returnPalindrome(number):
    rev=0
    while(number>0):
        rem=number%10
        rev=rev*10+rem
        number=number/10
    return rev

def isPalindrome(number):
    if(number==returnPalindrome(number)):
        return True
    return False

def main():
    number=input("Enter number to check if plaindrome")
    if(isPalindrome(number)):
        print("%d is palindrome"%number)
    else:
        print("%d is not palindrome"%number)

if __name__=='__main__':
    main()
