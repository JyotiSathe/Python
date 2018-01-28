#WAP to accept following values from user CRC,Lenght,Data,Flag,ProtocolType
#where CRC is 3 bits,length is 7 bits, data is 16 bits, flag is 2 bits, protocol
#type is 4 bits.

def create_packet(crc,length,data,flag,protocol_type):
    packet=0
    x=((1<<3)-1)
    crc=crc&x
    packet=crc

    x=((1<<7)-1)
    packet=packet<<7
    length=length&x
    packet=packet|length

    x=((1<<16)-1)
    packet=packet<<16
    data=data&x
    packet=packet|data

    x=((1<<2)-1)
    packet=packet<<2
    flag=flag&x
    packet=packet|flag

    x=((1<<4)-1)
    packet=packet<<4
    protocol_type=protocol_type&x
    packet=packet|protocol_type
    
    return packet

def decrypt_packet(packet):
    x=((1<<4)-1)
    protocol_type=packet&x
    packet=packet>>4

    x=((1<<2)-1)
    flag=packet&x
    packet=packet>>2

    x=((1<<16)-1)
    data=packet&x
    packet=packet>>16

    x=((1<<7)-1)
    length=packet&x
    packet=packet>>7

    x=((1<<3)-1)
    crc=packet&x
    packet=packet>>3
    
    return crc,length,data,flag,protocol_type

def main():
    crc=input("Enter CRC")
    length=input("Enter Length")
    data=input("Enter Data")
    flag=input("Enter Flag")
    protocol_type=input("Enter protocol type")
    packet=create_packet(crc,length,data,flag,protocol_type)
    print("Packet sent over network is")
    print(packet)

    crc,length,data,flag,protocol_type=decrypt_packet(packet)
    print("Packet received and it contains below information")
    print("crc={}".format(crc))
    print("length={}".format(length))
    print("data={}".format(data))
    print("flag={}".format(flag))
    print("protocol_type={}".format(protocol_type))

if __name__=='__main__':
    main()
