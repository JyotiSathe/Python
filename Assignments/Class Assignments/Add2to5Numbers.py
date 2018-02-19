# WAP to add 2,3,4 or 5 numbers

def add(a,b,c=0,d=0,e=0):
    return a+b+c+d+e

def main():
    print("add(10,20)= %d"%add(10,20))
    print("add(10,20,30)= %d"%add(10,20,30))
    print("add(10,20,30,40)= %d"%add(10,20,30,40))
    print("add(10,20,30,40,50)= %d"%add(10,20,30,40,50))

if __name__=='__main__':
    main()
