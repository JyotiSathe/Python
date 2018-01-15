def not_multiple_of_2_and_3(lb,ub):
    for i in range(lb,ub):
        if(i%2==0):
            if(i%3==0):
                continue
        else:
            print(i)

def main():
    lb,ub=input("Enter lower bond and upper bound")
    if(lb<ub):
        not_multiple_of_2_and_3(lb,ub)
    else:
        print("Enter proper range")

if __name__=='__main__':
    main()
