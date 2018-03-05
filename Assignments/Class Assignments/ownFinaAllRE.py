
import re
def findAll(pattern,str1):
    li=[]
    index=0
    while(not str1==""):
        x=re.search(pattern,str1)
        li.append((x.start()+index,x.end()+index))
        str1=str1[x.end():]
        index+=x.end()
    return li

def findAll_1(pattern,str1):
    li=[]
    index=0
    x=re.search(pattern,str1)
    while(not str1==""):
        li.append((x.start()+index,x.end()+index))
        str1=str1[x.end():]
        index+=x.end()
        x=re.search(pattern,str1)
    return li

def main():
    pattern=input("Enter pattern")
    str1=input("Enter String")
    print(findAll_1(pattern,str1))

if __name__=='__main__':
    main()
