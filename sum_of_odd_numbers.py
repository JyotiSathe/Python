#WAP to accept range from user and print sum of odd numbers in the given range
def check_range(lb,ub):
    if(lb<ub):
        return True
    return False

def isOdd(num):
    if(num&1==1):
        return True
    return False

def sum_of_odd_numbers(lb,ub):
    addition=0
    for i in range(lb,ub):
        if(isOdd(i)):
            addition=addition+i
    return addition
        
def main():
    lb,ub=input("Enter lb,ub for sum of odd numbers")
    if(check_range(lb,ub)):
        print(sum_of_odd_numbers(lb,ub))
    else:
        print("check range entered")
    
if __name__=='__main__':
    main()
