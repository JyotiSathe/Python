def turnOffRightmost1Bit(number):
    x=1
    while(x&number==0):
        x=x<<1
    return number&(~x)

def count1BitsInNumber(number):
    count=0
    while(number!=0):
        if(number&1==1):
            count+=1
        number=number>>1
    return count

def if2sPower(number):
    return (number&(number-1))==0

def check2sPowerDivisibiltyTest(number,divisor):
    if(if2sPower(divisor)):
        return (number&(divisor-1))==0
    else:
        print("Divisor not power of 2")

def turnOffnBits(number,pos,no_of_bits):
    x=(1<<(no_of_bits))-1
    x=x<<(pos-no_of_bits)
    return number&(~x)

def turnOnnBits(number,pos,no_of_bits):
    x=(1<<(no_of_bits))-1
    x=x<<(pos-no_of_bits)
    return number|x

def togglenBits(number,pos,no_of_bits):
    x=(1<<(no_of_bits))-1
    x=x<<(pos-no_of_bits)
    return number^x

def swapNBitsFromSamePosition(number1,number2,pos,no_of_bits):
    x=(1<<no_of_bits)-1
    x=x<<(pos-no_of_bits)
    number1_part=number1&x
    number2_part=number2&x
    number1=number1&(~x)
    number2=number2&(~x)
    number1=number1|number2_part
    number2=number2|number1_part
    return number1,number2
    
def swapNBitsFromDifferentPosition(number1,number2,pos1,pos2,no_of_bits):
    n=(1<<no_of_bits)-1
    x=n<<(pos1-no_of_bits)
    y=n<<(pos2-no_of_bits)
    number1_part=number1&x
    number2_part=number2&y
    number1=number1&(~x)
    number2=number2&(~y)
    if(pos1>pos2):
        number1_part=(number1_part>>(pos1-pos2))
        number2_part=(number2_part<<(pos1-pos2))
    else:
        number1_part=(number1_part<<(pos2-pos1))
        number2_part=(number2_part>>(pos2-pos1))
    number1=number1|number2_part
    number2=number2|number1_part
    return number1,number2
    
def go_to_choice(choice):
    if(choice==1):
        result=turnOffRightmost1Bit(input("Enter number"))
        print("Result is :{}".format(result))
    elif(choice==2):
        result=count1BitsInNumber(input("Enter number"))
        print("Result is :{}".format(result))
    elif(choice==3):
        result=if2sPower(input("Enter number"))
        if(result):
            print("Number is 2's power")
        else:
            print("Number is not of 2's power")
    elif(choice==4):
        number=input("Enter number")
        divisor=input("Enter divisor")
        result=check2sPowerDivisibiltyTest(number,divisor)
        if(result):
            print("{} is divisible by {}".format(number,divisor))
        else:
            print("{} is not divisible by {}".format(number,divisor))
    elif(choice==5):
        number=input("Enter number")
        pos=input("Enter position from which you want you want to off the bit")
        no_of_bits=input("Enter how many bits to turn off")
        result=turnOffnBits(number,pos,no_of_bits)
        print("Result is :{}".format(result))
    elif(choice==6):
        number=input("Enter number")
        pos=input("Enter position from which you want you want to off the bit")
        no_of_bits=input("Enter how many bits to turn off")
        result=turnOnnBits(number,pos,no_of_bits)
        print("Result is :{}".format(result))
    elif(choice==7):
        number=input("Enter number")
        pos=input("Enter position from which you want you want to off the bit")
        no_of_bits=input("Enter how many bits to turn off")
        result=togglenBits(number,pos,no_of_bits)
        print("Result is :{}".format(result))
    elif(choice==8):
        number1=input("Enter number1")
        number2=input("Enter number2")
        pos=input("Enter position")
        no_of_bits=input("Enter number of bits")
        n1,n2=swapNBitsFromSamePosition(number1,number2,pos,no_of_bits)
        print(n1)
        print(n2)
    elif(choice==9):
        number1=input("Enter number1")
        number2=input("Enter number2")
        pos1=input("Enter position for first number")
        pos2=input("Enter position for second number")
        no_of_bits=input("Enter number of bits")
        n1,n2=swapNBitsFromDifferentPosition(number1,number2,pos1,pos2,no_of_bits)
        print(n1)
        print(n2)
    else:
        return
        
def get_choice():
    print("**********************************************")
    return input("Which operations you want to perform")

def Menu():
    print("*********************MENU*********************")
    print("1:turnOff Righmost 1 bit")
    print("2:Count number of 1 bits in a number")
    print("3:Check if entered number is 2's power")
    print("4:Check if number is divisible by provided 2's power divisor")
    print("5:turnOff given n bits from given position in a number ")
    print("6:turnOn given n bits from given position in a number ")
    print("7:toggle given n bits from given position in a number ")
    print("8:Swap n bits from given position in 2 number")
    print("9:Swap n bits from different given positions in 2 numbers ")
    print("10:Exit")

def main():
    print("Hey!! Let's do some practise on bitwise operations")
    Menu()     
    choice=get_choice()
    while(choice>0 and choice<10):
        go_to_choice(choice)
        #Menu()
        choice=get_choice()

if __name__=='__main__':
    main()
