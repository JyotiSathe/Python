
import os
import sys

c_count = 0
cpp_count = 0
py_count = 0
h_count = 0
other_count = 0
def callback_func(arg,directory,files):
    global c_count
    global cpp_count
    global py_count
    global h_count
    global other_count
    for file1 in files:
        print file1
        if file1.endswith(arg[0]):
            py_count+=1
        elif file1.endswith(arg[1]):
            c_count+=1
        elif file1.endswith(arg[2]):
            cpp_count+=1
        elif file1.endswith(arg[3]):
            h_count+=1
        else:
            other_count+=1

def main():
    os.path.walk("F:\Python\Python-master\generic",callback_func,(".py",".c",".cpp",".h"))
    print "Python :", py_count, "C :", c_count, "CPP: ", cpp_count, "Header: ", h_count, "Other: ", other_count
    
if __name__=='__main__':
    main()
