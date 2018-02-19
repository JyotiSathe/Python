#WAP a program to accept number of rows and print below pattern
#        *
#      * * *
#    * * * * *
#  * * * * * * *
#* * * * * * * * *
def pattern_display(rows):
    for i in range(rows):
        for k in range(-(i*1)+(rows-1)):
            print " ",
        for j in range(i*2+1):
            print "*",
        print

def main():
    rows=input("Enter number of rows for pattern display")
    pattern_display(rows)

if __name__=='__main__':
    main()
