#WA function which accepts a list and an element to be appended, if the element
#to be appended is a container then input list should be extended or it should get appended

def add_elements_to_list(l1,element):
    print(type(l1))
    print(type(element))
    if(type(element)==list):
        l1.extend(element)
    else:
        l1.append(element)

    return l1

def main():
    print(add_elements_to_list([1,2,3],4))
    print(add_elements_to_list([1,2,3],[4]))

if __name__=='__main__':
    main()
