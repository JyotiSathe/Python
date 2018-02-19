


def getCountOfCharWithIndexDict(str1):
    result_dict={}
    index_dict={}
    i=0
    while i<len(str1):
        char=str1[i]
        count=1
        index_dict[i]=count
        result_dict[char]=index_dict
        while():
            
        print index_dict
        print result_dict
        i+=1

def main():
    str1=input("Enter string")
    result_dict=getCountOfCharWithIndexDict(str1)
    print result_dict

if __name__=='__main__':
    main()
