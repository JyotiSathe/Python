#Program of demo of Keyword Arguments
def KeywordArgumentsDemo(a,b):
    print("Positional Arguments are a={} and b={}".format(a,b))

def main():
    KeywordArgumentsDemo(b=10,a=20)

if __name__=='__main__':
    main()
