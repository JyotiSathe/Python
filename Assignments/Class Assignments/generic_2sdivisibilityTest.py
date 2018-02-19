import isRaiseToPower2
def generic_2sdivisibilityTest(number,divisor):
    return (number&(divisor-1))==0

def main():
    number=input("Enter number")
    divisor=input("Enter divisor in 2s power")
    if(isRaiseToPower2.isRaiseToPower2(divisor)):
        if(generic_2sdivisibilityTest(number,divisor)):
            print("divisible")
        else:
            print("not divisible")
    else:
        print("divisor not power of 2")
        
if __name__=='__main__':
    main()
