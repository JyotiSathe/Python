import os
import sys

def main():
    c_count = 0
    cpp_count = 0
    py_count = 0
    h_count = 0
    other_count = 0
    dir_count=0
    path="F:\Python\Python-master\generic"
    print (path)
    for root, dirs, files in os.walk(path):
        for file1 in files:
            if file1.endswith(".py"):
                py_count+=1
            elif file1.endswith(".c"):
                c_count+=1
            elif file1.endswith(".cpp"):
                cpp_count+=1
            elif file1.endswith(".h"):
                h_count+=1
            else:
                other_count+=1
        for dir1 in dirs:
            dir_count+=1
        
    print ("Python :", py_count, "\nC :", c_count, "\nCPP: ", cpp_count, "\nHeader: ", h_count, "\nOther: ", other_count, "\nDirectory Count:", dir_count)
    
if __name__=='__main__':
    main()
