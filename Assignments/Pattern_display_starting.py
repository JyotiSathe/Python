'''WAP to accept number of rows from user and print below patterns
First Pattern
*
* *
* * *
* * * *
Second Pattern
* * * *
* * *
* *
*
Third Pattern
A
AB
ABC
ABCD
Fourth Pattern
A
A A
A A A
A A A A
Fifth Pattern
1
1 2
1 2 3
1 2 3 4
'''

def display_pattern1(rows):
    for i in range(rows):
        for j in range(0,i+1):
            print '*',
        print

def display_pattern1_1(rows):
    for i in range(rows):
        for j in range(0,i+1):
            print 'A',
        print

def display_pattern1_2(rows):
    for i in range(rows):
        for j in range(0,i+1):
            print j+1,
        print

def display_pattern2(rows):
    for i in range(rows,0,-1):
        for j in range(i,0,-1):
            print '*',
        print

def display_pattern3(rows):
    input_str="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(rows):
        print input_str[0:i+1]

def main():
    rows=input("Enter number of rows to be printed in pattern")
    print("First Pattern")
    display_pattern1(rows)
    print("Second Pattern")
    display_pattern2(rows)
    print("Third Pattern")
    display_pattern3(rows)
    print("Fourth Pattern")
    display_pattern1_1(rows)
    print("Fifth Pattern")
    display_pattern1_2(rows)
    
if __name__=='__main__':
    main()
