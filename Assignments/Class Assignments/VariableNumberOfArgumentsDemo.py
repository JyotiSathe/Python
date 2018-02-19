#Program of demo of Variable Arguments
def VariableNumberOfArgumentsDemo(*args):
    print(type(args))
    for i in args:
        print i,

def main():
    VariableNumberOfArgumentsDemo(1,2,3,4)
    print
    VariableNumberOfArgumentsDemo(11,23,24,56,55,"hi","bye")

if __name__=='__main__':
    main()
