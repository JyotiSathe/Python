#WAP to accept a string from user and display a string made of first 2 characters and last 2 characters
def two_letters_display(input_str):
    return input_str[0:2]+input_str[-2:]
def main():
    input_str=input("Enter String")
    output_str=two_letters_display(input_str)
    print(output_str)
if __name__=='__main__':
    main()
