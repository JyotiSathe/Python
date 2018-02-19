import os
import sys

c_count = 0
cpp_count = 0
py_count = 0
h_count = 0
other_count = 0

def main():
    for root, dirs, files in os.walk("F:\Python\Python-master\generic"):
        print (root)
        global c_count
        global cpp_count
        global py_count
        global h_count
        global other_count
        for file1 in files:
            print (file1)
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
        
    print ("Python :", py_count, "C :", c_count, "CPP: ", cpp_count, "Header: ", h_count, "Other: ", other_count)
    
if __name__=='__main__':
    main()
