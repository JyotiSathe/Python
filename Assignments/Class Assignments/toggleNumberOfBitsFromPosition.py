#WAP to accept a number, position and number of bits to be toggled from the given position.
#toggle respective bits from the given position and display the result

def toggleNumberOfBitsFromPosition(number,pos,no_of_bits):
    x=(1<<no_of_bits)-1
    x=x<<(pos-no_of_bits)
    return number^(x)

def main():
    number=input("Enter number")
    pos=input("Enter position")
    no_of_bits=input("Enter number of bits")
    if(pos>=no_of_bits):
        print(toggleNumberOfBitsFromPosition(number,pos,no_of_bits))
    else:
        print("you have entered no of bits greater than position")

if __name__=='__main__':
    main()
