#program to accept string from user and check if palindrome
def main():
    x=input("Enter string to check if palindrome\n")
    if(x==x[::-1]):
        print("%s is palindrome"%x)
    else:
        print("%s is not palindrome"%x)

def isPalindrome(input_str):
    return input_str==input_str[::-1]

if __name__=='__main__':
    #main()
    input_str=input("Enter string to check if plaindrome")
    
    if(isPalindrome(input_str)):
        #print(input_str+" is palindrome")
        var=""
    else:
        #print(input_str+" is not palindrome")
        var=" not"

print(input_str+" is"+var+" palindrome")
