#WAP to accpet directory path from user and type of files to be deleted
#recursively from the given directory

import os
def removeFiles(arg,directory,files):
    count=0
    print("In directory "+directory)
    for file1 in files:
        if file1.endswith(arg):
            count+=1
            print ("removing file "+directory+"/"+file1)
            os.remove(directory+"/"+file1)    
    else:
        if count==0:
            print ("No "+arg+" Files exists")

def main():
    path=input("Enter path of a file from which to delete files from")
    type_of_file=input("Enter type of files to remove")
    os.path.walk(path,removeFiles,type_of_file)

if __name__=='__main__':
    main()
