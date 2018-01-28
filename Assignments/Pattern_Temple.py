#WAP to accept number of rows from user and print below pattern.
#* * * * * * *
#* * *   * * *
#* *       * *
#*           *

def print_temple_star(rows):
    for i in range(rows):
        for j in range(-rows+1,rows):
            if(i>=abs(j)+1):
                print " ",
            else:
                print "*",
        print

def main():
    rows=input("Enter number of rows")
    print_temple_star(rows)

if __name__=='__main__':
    main()
