#WAP to accept number of rows from user and print below pattern
#      A
#    B A B
#  C B A B C
#D C B A B C D


def print_letter_triangle(rows):
    for i in range(rows):
        x=65
        for k in range(abs(rows-i)-1):
            print " ",
        for j in range(-i,i+1):
            print chr(x+abs(j)),
        print

def main():
    rows=input("Enter number of rows")
    print_letter_triangle(rows)

if __name__=='__main__':
    main()
