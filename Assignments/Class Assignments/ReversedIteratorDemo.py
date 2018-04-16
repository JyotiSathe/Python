
class ReferenceCount:
    def __init__(self,start):
        self.start=start

    def __reversed__(self):
        while self.start>0:
            yield self.start
            self.start-=1    

    def __iter__(self):
        return self

    '''def __reversed__(self):
        start=1
        while start<=self.start:
            yield start
            start+=1'''

def main():
    x=ReferenceCount(10)
    #for y in x:
    #    print next(y)
    for y in reversed(x):
        print y

if __name__=='__main__':
    main()
