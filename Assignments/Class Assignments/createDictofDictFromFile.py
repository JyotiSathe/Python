#WAP to accept a file from user in below format and make a dictionary of dictionary
#out of it and print it

def createDictOfDictFromFile(filename):

    result={}
    fd=open(filename)
    line=fd.readline()
    section_name=""
    section_details={}
    section_found=False
    while line!="":
        lineStr=str(line)
        if lineStr.startswith("#") or lineStr.startswith("\n"):
            line=fd.readline()
            continue
        if lineStr.startswith("["):
            print line
            if section_found==True:
                print "section true"
                print line
                result[section_name]=section_details
                section_found=False
            if section_found==False:
                print "section false"
                print line
                section_name=lineStr[1:-2]
                section_found=True
                section_details={}
        elif section_found==True:
            print "section found"
            print line
            split_line=lineStr.split('=')
            if '#' in split_line[1]:
                split_line[1]=split_line[1].split('#')[0]
            if '\n' in split_line[1]:
                split_line[1]=split_line[1].split('\n')[0]
            section_details[split_line[0]]=split_line[1]
        else:
            result[section_name]=section_details
        line=fd.readline()
    return result

def main():
    filename=input("Enter filename")
    output=createDictOfDictFromFile(filename)
    print output
    

if __name__=='__main__':
    main()
