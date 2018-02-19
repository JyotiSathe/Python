#WAP to accept 2 numbers from user accept position and number of bits to be swapped
#from the given 2 numbers

def swapNumberOfBitsFromPosition(number1,number2,pos,no_of_bits):
    x=(1<<no_of_bits)-1
    x=x<<(pos-no_of_bits)

    number1_part=x&number1
    number2_part=x&number2

    number1=number1&(~x)
    number2=number2&(~x)

    number1=number1|number2_part
    number2=number2|number1_part

    return number1,number2

def main():
    number1,number2=swapNumberOfBitsFromPosition(217,198,5,4)
    print(number1)
    print(number2)

if __name__=='__main__':
    main()
