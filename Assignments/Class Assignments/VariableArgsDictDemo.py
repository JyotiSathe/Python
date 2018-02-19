#Program of demo of Variable Arguments Dictionary
def varArgDict(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

def main():
    varArgDict(name="Jyoti",hobby="Programming")

if __name__=='__main__':
    main()
