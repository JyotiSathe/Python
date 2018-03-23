
import re
def countPattern(pattern,str1):
    li=[]
    index=0
    count=0
    while(not str1==""):
        x=re.search(pattern,str1)
        #li.append((x.start()+index,x.end()+index))
        str1=str1[x.end():]
        index+=x.end()
        count+=1
    return count
    

def main():
    pattern=input("Enter pattern")
    str1=input("Enter String")
    count=countPattern(pattern,str1)
    print count

if __name__=='__main__':
    main()
