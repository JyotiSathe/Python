#Program of demo of Dafault Arguments
def add(a,b=100):
    return a+b

def main():
    print("add(10) %d"%add(10))
    print("add(30) %d"%add(30))
    print("add(20,30) %d"%add(20,30))

def DefualtArgumentsDemo(a,b=100):
    print("Default Arguments are a={} and b={}".format(a,b))

def main1():
    DefualtArgumentsDemo(10)
    DefualtArgumentsDemo(20)
    DefualtArgumentsDemo(20,30)

if __name__=='__main__':
    main1()
