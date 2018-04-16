class Test:
    @classmethod
    def bar(cls):
        print (id(cls))
        print ("Static method bar")

def main():
    Test.bar()
    print(id(Test))

if __name__=='__main__':
    main()
