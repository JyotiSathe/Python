#WAP to accept string as below and output should be its count after character
#aabbcccddabbb
#a2b2c3d2a1b3

def GenerateStringOfCounts(str1):
    i=0
    result_str=""
    while i<len(str1):
        char=str1[i]
        count=1
        while((i+1)<len(str1) and str1[i+1]==char):
            count+=1
            i+=1
        result_str+=char+str(count)
        i+=1
    return result_str

def charactersWithCount(str1):
    result_string=str1[0]
    for i in range(0,len(str1)-1):
        print i
        char=str1[i]
        print char
        tempcount=1
        if(str1[i+1]==char):
            
            print "in if"
            tempcount+=1
            result_string=result_string+str(tempcount)
            print result_string
            
        else:
            result_string+=char

    return result_string
def main():
    str1=input("Enter string")
    result_str=charactersWithCount(str1)
    print result_str

if __name__=='__main__':
    main()
