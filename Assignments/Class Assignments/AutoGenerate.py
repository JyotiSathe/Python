class AutoGenerate:
    def __init__(self,start,stop,step=1):
        self.start=start
        self.stop=stop
        self.step=step

    def __next__(self):
        self.start+=self.step
        if self.start>=self.stop:
            raise StopIteration
        yield self.start

    def next(self):
        return self.__next__()

    def __iter__(self):
        return self

def main():
    x=AutoGenerate(0,100,5)
    z=iter(x)
    for i in z:
        print x.next().next()


if __name__=='__main__':
    main()
