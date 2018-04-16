#WA decorator function which adds init and del method to the classes on
#which it is applied

def InitDecorator(cls):
    def __init__(self):
        print "initialize"

    def __del__(self):
        print "deinitialize"
    
    cls.__init__=__init__
    cls.__del__=__del__
    return cls

@InitDecorator
class Temp(object):
    def Display(self):
        pass

def main():
    print Temp.__dict__
    obj=Temp()

if __name__=='__main__':
    main()
