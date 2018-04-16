class AutoIterate:

    def __init__(self,start,end,step=1):
        self.start=start
        self.end=end
        self.step=step

    def __next__(self):
        self.start+=self.step
        if self.start>=self.end:
            raise StopIteration
        return self.start

    def next(self):
        return self.__next__()
            
    def __iter__(self):
        return self

def main():
    x=AutoIterate(0,100,5)
    for y in x:
        print y
    #z=iter(x)
    #for i in z:
    #    print i

if __name__=='__main__':
    main()
