#WAP to print dictionary of character and its count from a string

def getDictOfCharWithCount(str1):
    result_dict={}
    i=0
    while i < len(str1):
        char=str1[i]
        count=0
        j=0
        while j<len(str1):
            if(char==str1[j]):
                count+=1
            j+=1
        result_dict[char]=count
        i+=1
    return result_dict

def getDictofCountOfChar(str1):
    result_dict={}
    for i in str1:
        if(result_dict.has_key(i)):
            result_dict[i]=result_dict[i]+1
        else:
            result_dict[i]=1
    return result_dict
        
def main():
    str1=input("Enter string")
    result_dict=getDictofCountOfChar(str1)
    print result_dict

if __name__=='__main__':
    main()


