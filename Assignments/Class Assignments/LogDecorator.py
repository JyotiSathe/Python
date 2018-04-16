'''
    Using Decorator
'''
import time
def LogDecorator(func):
    
    def log(args):
        return func(str(time.time())+":"+args)
    return log

@LogDecorator
def Logger(data):
    print ("Logged {}".format(data))

Logger("Hi")
