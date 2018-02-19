#WAP which copies source file to destination file, source file name and
#destination file name should come as command line argument
#copy.py <src_file> <dest_file>
import sys
import argparse

def copyFile(src_file,dest_file,n):
    srcFd=open(src_file)
    destFd=open(dest_file,"w")
    
    if n==0:
        line=srcFd.readline()
        while line!="":
            destFd.write(line)
            line=srcFd.readline()
    else:
        line =srcFd.readline()
        while n!=0 and line != "" :
            destFd.write(line)
            line=srcFd.readline()
            n-=1
        destFd.flush()
    srcFd.close()
    destFd.close()

    
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-i",type=str,help="Input/source File Name")
    parser.add_argument("-d",type=str,help="Destination File Name")
    parser.add_argument("-n",type=int,help="Number of lines to Copy, default=0(complete file)",default=0)
    args=parser.parse_args()
    print type(args.n)
    print args
    copyFile(args.i,args.d,args.n)

if __name__=='__main__':
    main()
