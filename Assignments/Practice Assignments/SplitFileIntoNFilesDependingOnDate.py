def splitFiles(filename):
    fd=open(filename)
    line=fd.readline()
    line=fd.readline()
    prev_date=line.split(",")[2]
    curr_date=line.split(",")[2]
    filename1="assetId"+curr_date.rstrip()+".csv"
    print filename1
    fd1=open(filename1,"w")
    flag=False
    c1=0
    while line!="":
        if prev_date==curr_date:
            fd1.write(line)
        else:
            prev_date=line.split(",")[2]
            filename1="assetId"+curr_date.rstrip()+".csv"
            print filename1
            fd1=open(filename1,"w")
            fd1.write(line)
        line=fd.readline()
        curr_date=line.split(",")[2]

def main():
    filename=input("Enter Filename")
    splitFiles(filename)

if __name__=='__main__':
    main()
