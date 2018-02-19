#WAP to accept 2 numbers from user accept 2 positions and number of bits to be swapped
#from the given 2 numbers

def swapNumberOfBitsFromDiffPosition(number1,number2,pos1,pos2,no_of_bits):
    x=(1<<no_of_bits)-1
    n1=x<<(pos1-no_of_bits)
    n2=x<<(pos2-no_of_bits)
    
    number1_part=n1&number1
    number2_part=n2&number2

    number1=number1&(~n1)
    number2=number2&(~n2)

    if(pos1>pos2):
        number1=number1|(number2_part<<(pos1-pos2))
        number2=number2|(number1_part>>(pos1-pos2))
    else:
        number1=number1|(number2_part>>(pos2-pos1))
        number2=number2|(number1_part<<(pos2-pos1))
    return number1,number2

def main():
    number1,number2=swapNumberOfBitsFromDiffPosition(217,198,7,6,4)
    print(number1)
    print(number2)

if __name__=='__main__':
    main()
