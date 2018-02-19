def fromkeys_my(x,y):
    temp={}
    if(type(y)==int):
        temp=dict.fromkeys(x,y)
    else:
        i=0
        if(len(y)>=len(x.keys())):
            for key in x:
                temp[key]=y[i]
                i+=1
        elif(len(y)<len(x.keys())):
            for key in x:
                if(len(y)!=i):
                    temp[key]=y[i]
                else:
                    temp[key]="None"
                i+=1
            
    return temp

def fromkeys(input_dict,output_dict_values):
    result_dict={}
    if(type(output_dict_values)==list or type(output_dict_values)==tuple):
        keys_list=input_dict.keys()
        values_length=len(output_dict_values)
        for i in range(len(keys_list)):
            if i<values_length:
                result_dict[keys_list[i]]=output_dict_values[i]
            else:
                result_dict[keys_list[i]]="None"
    else:
        result_dict=dict.fromkeys(input_dict,output_dict_values)
    return result_dict

def main():
    #x={1:2,2:3,3:4}
    x=input("Enter dictionary")
    y=input("Enter what you want to enter as values")
    result=fromkeys(x,y)
    print result

if __name__=='__main__':
    main()
