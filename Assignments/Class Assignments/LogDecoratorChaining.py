'''
    Using Decorator Chaining
'''
import time
def LogDecorator(func):
    print ("Outer Log Decorator")
    def log(args):
        print ("Log Decorator")
        return func(str(time.time())+" "+args)
    return log

def NameDecorator(func):
    print ("Outer Name Decorator")
    def log(args):
        print ("Name Decorator")
        return func("Trinaha Solutions:"+args)
    return log

@LogDecorator
@NameDecorator
def Logger(data):
    print ("Logged {}".format(data))

def main():
    Logger("TOP")
    time.sleep(1)
    Logger("PS")

if __name__=='__main__':
    main()
