#WAP to accpet a string from user and print alternate characters in it starting with first character

def alternate_letter(input_str):
    return input_str[0::2]
def main():
    input_str=input("Enter String")
    output_str=alternate_letter(input_str)
    print(output_str)
if __name__=='__main__':
    main()
