#WAP to accept 2 directory names from user and check if both of them contains
#same files
import os
list1 = []
list2 = []
def getFilesList(arg,directory,files):
    global list1
    global list2
    for file1 in files:
        if(arg=="first"):
            if(os.path.isdir(directory+"/"+file1)):
                continue
            else:
                list1.append(file1)
        elif(arg=="second"):
            if(os.path.isdir(directory+"/"+file1)):
                continue
            else:
                list2.append(file1)
        else:
            print("NA")

def if2DirectoriesSame(l1,l2):
    ifSame=False
    if(len(l1)==len(l2)):
        if(l1==l2):
            ifSame=True
    return ifSame
        
def main():
    dir1=input("Enter first directory path")
    dir2=input("Enter second directory path")
    os.path.walk(dir1,getFilesList,"first")
    os.path.walk(dir1,getFilesList,"second")
    print (list1)
    print (list2)
    if(if2DirectoriesSame(list1,list2)):
        print ("Directories Same")
    else:
        print ("Directories Different")

if __name__=='__main__':
    main()
