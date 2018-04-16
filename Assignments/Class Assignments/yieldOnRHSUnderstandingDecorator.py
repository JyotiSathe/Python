'''
    Understanding Decorator
'''
def ToUpper():
    while True:
        input_string=yield
        print (input_string.upper())
        #yield input_string.upper()

def Wrapper(func):
    def foo(*args):
        z=func()
        next(z)
        return z
    return foo

@Wrapper
def ToLower():
    while True:
        input_string=yield
        print (input_string.lower())

def main():
    z=ToUpper()
    next(z)
    z.send("Hello")

def main1():
    toupper=Wrapper(ToUpper)
    z=toupper()
    z.send("Hello Jyoti,")
    #next(z)
    z.send("Good Morning!!!")
    print ""
    z=ToLower()
    z.send("Hello Jyoti,")
    z.send("Good Morning!!!")

if __name__=='__main__':
    main1()
