def adder(no):
    def add(number):
        return no+number
    return add

    '''def add2(n1,n2):
        return no+n1+n2
    return add,add2'''

def main():
    adder_10=adder(10)
    print type(adder_10)
    print adder_10(100)
    print adder_10(25)
    #print adder_10(20,13)

if __name__=='__main__':
    main()
