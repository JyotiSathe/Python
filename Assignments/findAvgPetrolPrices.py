#WAP to find avergae of petrol prices from file

def findAvgPetrolPrices(filename):
    fd=open(filename)
    line=fd.readline()
    mh_sum=0
    goa_sum=0
    kn_sum=0
    count=0
    mh_avg=0
    goa_avg=0
    kn_avg=0
    while line!="":
        split_str=str(line).split(" ")
        mh_sum+=float(split_str[2])
        goa_sum+=float(split_str[3])
        kn_sum+=float(split_str[4])
        count+=1
        line=fd.readline()
    mh_avg=mh_sum/count
    goa_avg=goa_sum/count
    kn_avg=kn_sum/count
    return mh_avg,goa_avg,kn_avg

def main():
    filename=input("Enter filename")
    mh_avg,goa_avg,kn_avg=findAvgPetrolPrices(filename)
    print("Average petrol price in Maharashtra={}".format(mh_avg))
    print("Average petrol price in Goa={}".format(goa_avg))
    print("Average petrol price in Karnataka={}".format(kn_avg))

if __name__=='__main__':
    main()
