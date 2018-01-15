#WAP to accept 2 string from user and swap first 2 characters of each of them
#
#Enter 1st String"Saoti"
#Enter 2nd String"Jythe"
#Jyoti
#Sathe
def swap_first_two(first,second):
    print(second[0:2]+first[2:])
    print(first[0:2]+second[2:])
def main():
    first=input("Enter 1st String")
    second=input("Enter 2nd String")
    swap_first_two(first,second)
if __name__=='__main__':
    main()
