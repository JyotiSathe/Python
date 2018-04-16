#WAP to validate an email id using regular expression

import re

def validateEmail():
    emailPattern=re.compile("([\w\.-]+)@([\w]+)\.([\w]+)")
    return emailPattern

def main():
    emailList=['jyotisathe1138@gmail.com','jyotisathe1138@gmail',
               'xyz@gmail@yahoo@gmail.com','abc189@yahoo.co.in']

    for i in emailList:
        obj=validateEmail().search(i)
        print i
        if obj:
            print "Match"
            print obj.groups()
        else:
            print "No match"
if __name__=='__main__':
    main()
