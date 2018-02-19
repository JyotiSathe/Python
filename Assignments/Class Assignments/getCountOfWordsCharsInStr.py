#WAP to accept a string from user and print number of characters and words in it
def getCountOfWordsAndChars(s):
    countChr=0
    countWord=0
    for i in range(len(s)):
        if(s[i]!=" "):
            countChr=countChr+1
        else:
            countWord+=1
    if(not s.endswith(" ")):
        countWord+=1
    #return "Count of character is "+str(countChr)+"\n"+"Count of words is "+str(countWord)
    return countChr,countWord

def main():
    s=input("Enter a sentence")
    #output=getCountOfWordsAndChars(s)
    #print output
    chrCount,wordCount=getCountOfWordsAndChars(s)
    print("Count of character is {}\n Count of words is {}".format(chrCount,wordCount))
    
if __name__=='__main__':
    main()
