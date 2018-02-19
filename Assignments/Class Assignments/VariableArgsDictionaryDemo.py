#Program of demo of Variable Arguments Dictionary
def VariableArgsDictionaryDemo(a,b,c,*args,**kwargs):
    print(a,b,c)
    print(type(args))
    for x in args:
        print x
    print(type(kwargs))
    for key in kwargs:
        print(key,kwargs[key])

def main():
    VariableArgsDictionaryDemo(1,2,3,7,8,9,10,name="Jyoti",hobby="Programming")

if __name__=='__main__':
    main()
