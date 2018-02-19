#WAP a program to accept number of rows and print below pattern
#      *
#    * *
#  * * *
#* * * *
def bottom_space_star(rows):
    for i in range(1,rows+1):
        for j in range(rows-i):
            print " ",
        for k in range(i):
            print "*",
        print


def main():
    rows=input("Enter number of rows")
    bottom_space_star(rows)

if __name__=='__main__':
    main()
