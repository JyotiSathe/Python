class FileIterator:
    def __init__(self,filename):
        self.fd=open(filename)

    def __iter__(self):
        return self
    
    def next(self):
        line=self.fd.readline()
        return line


def main():
    x=FileIterator(input("Enter Filename"))
    print x.next()
    print x.next()

if __name__=='__main__':
    main()
