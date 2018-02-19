#WAP to accept lower and upper bound and print all odd numbers in it
def print_odd(start_range,end_range):
    if(start_range>end_range):
        print("End range is smaller than start range, please enter proper range")
    else:
        print("Odd numbers in range {} to {} is".format(start_range,end_range))
        for x in range(start_range,end_range):
            if((x&1)==1):
                print(x)
                
def main():
    print("Enter range to print odd numbers")
    start_range=input("Enter starting range: ")
    end_range=input("Enter ending range: ")
    print_odd(start_range,end_range)

def isOdd(num):
    return num%2==1

def isOddBitwise(num):
    return (num&1)==1

def main2():
    print("Enter range to print odd numbers")
    lb,ub=input("Enter lower bound and upper bound")
    #lb,ub=10,20
    if(lb>ub):
        print("Range entered incorrectly")
    else:
        print("Odd numbers in range {} to {} is".format(lb,ub))
        for x in range(lb,ub):
            if isOddBitwise(x):
                print("%d is odd number"%x)
    
if __name__=='__main__':
    main2()

'''
Enter range to print odd numbers
Enter lower bound and upper bound10,20
Odd numbers in range 10 to 20 is
11 is odd number
13 is odd number
15 is odd number
17 is odd number
19 is odd number
>>> 
'''
