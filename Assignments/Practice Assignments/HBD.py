

def pattern_display(word):
    for i in range(len(word)+1):
        for j in range(i):
            print word[j],
        print

def main():
    name=input("Enter your name in double quotes")
    print "    ^"
    print "    *"
    print "    *"
    for i in range(0,3):
        print "*********"

    l1=['Happy','Birthday','Emma']
    for i in l1:
        pattern_display(i);
    if not name.upper()=="EMMA":
        print "-From {}".format(name)
    
if __name__=='__main__':
    main()
