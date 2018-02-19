#WAP to accept number of rows from user and print a diamond
#   *
#  ***
# *****
#  ***
#   *
def print_diamond(rows):
    for i in range(-rows+1,rows):
        for k in range(abs(i)):
            print " ",
        for j in range((rows*2-1)-abs(i*2)):
            print "*",
        print

def main():
    rows=input("Enter number of rows to be printed")
    print_diamond(rows)

if __name__=='__main__':
    main()
