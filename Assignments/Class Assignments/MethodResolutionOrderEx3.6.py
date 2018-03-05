


class Base():

    def bar(self):
        print ("Base bar")

    def foo(self):
        print ("Base foo")

class Derived1(Base):
    def bar(self):
        print("Derived1 bar")

class Derived2(Base):
    def foo(self):
        print ("Derived2 foo")

class Child(Derived1,Derived2):
    pass

def main():
    x=Child()
    x.foo()
    x.bar()
    y=Base()
    y.foo()
    y.bar()

if __name__=='__main__':
    main()
