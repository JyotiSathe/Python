# WAP to multiply 2,3,4 or 5 numbers

def multiply(a,b,c=1,d=1,e=1):
    return a*b*c*d*e

def main():
    print("multiply(10,20)= %d"%multiply(10,20))
    print("multiply(10,20,30)= %d"%multiply(10,20,30))
    print("multiply(10,20,30,40)= %d"%multiply(10,20,30,40))
    print("multiply(10,20,30,40,50)= %d"%multiply(10,20,30,40,50))

if __name__=='__main__':
    main()
