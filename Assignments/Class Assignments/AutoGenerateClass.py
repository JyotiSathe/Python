class AutoGenerate:
    def __init__(self,start,stop,step=1):
        self.start=start
        self.stop=stop
        self.step=step

    def Next(self):
        self.start+=self.step
        if self.start>=self.stop:
            raise StopIteration
        yield self.start

    def next(self):
        return self.Next().next()

    def __next__(self):
        return self.Next().__next__()

    #def __iter__(self):
    #    return self

def main():
    x=AutoGenerate(0,100,5)
    #for sets iterator so if need to give for needs to have iter method
    #for y in x:
    #    print y
    y=x.next()
    print (y)

    

if __name__=='__main__':
    main()
