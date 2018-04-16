#WAP to implement exception handling
import sys
def division(number,divisor):
    try:
        result=number/divisor
        print result
    
    except ArithmeticError as e:
        print ("ArithmeticError ",e)
        sys.exit(0)
    except BaseException as e:
        print ("BaseException ",e)
        sys.exit(0)
    else:
        print ("Executes if no exception")
    finally:
        print ("Executes Always")
    '''except ZeroDivisionError as e:
        print ("Divided by Zero ",e)
        sys.exit(0)'''

def main():
    number=input("Enter number")
    divisor=input("Enter divisor")
    division(number,divisor)
    number=input("Enter number")
    divisor=input("Enter divisor")
    division(number,divisor)

if __name__=='__main__':
    main()
