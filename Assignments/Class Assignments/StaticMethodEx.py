class Test:
    @staticmethod
    def bar():
        print ("Static method bar")

def main():
    Test.bar()

if __name__=='__main__':
    main()
