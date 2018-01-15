#WAP to accept number of rows from user and print below pattern
#A
#A B
#A B C
#A B C D
def pattern_display(rows):
    for i in range(1,rows+1):
        x=65
        for j in range(i):
            print chr(x+j),
        print

def pattern_display_1(rows):
    x=64
    for i in range(rows):
        for j in range(i+1):
            x=x+1
            print chr(x),
        print

def main():
    rows=input("Enter number of rows")
    pattern_display(rows)
    #pattern_display_1(rows)

if __name__=='__main__':
    main()
