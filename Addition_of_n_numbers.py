def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

def main():
    n=input("Enter how many elements")
    l=[]
    for i in range(n):
        num=input("Enter number %d "%(i+1))
        l.append(num)
    sum=add(*l)
    print("Addition is ",sum)
    
if __name__=='__main__':
    main()
