#WAP to program to add n numbers
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

def main():
    print(add(1,2,3,4,5,6,7,8,9,10))

if __name__=='__main__':
    main()
