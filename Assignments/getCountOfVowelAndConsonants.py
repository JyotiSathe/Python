#WAP to accept a string from user and print how many vowels and consonants present in that string

def getcount(input_str):
    vowel_count=0
    consonant_count=0
    length=len(input_str)
    for i in range(length):
        if(input_str[i]==" "):
            continue
        elif(input_str[i] in ['a','e','i','o','u']):
            vowel_count=vowel_count+1
        else:
            consonant_count=consonant_count+1
    print("Vowel count is %d"%vowel_count)
    print("Consonant count is %d"%consonant_count)

def main():
    input_str=input("Enter string")
    getcount(input_str)

if __name__=='__main__':
    main()
