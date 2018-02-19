#WAP to accept following values from user crc,length,data and flag where crc is
#5 bits length is 8 bits, data is 18 bits and flag is 1 bit

def create_packet(crc,length,data,flag):
    packet=0
    x=((1<<5)-1)
    crc=crc&x
    packet=crc

    x=((1<<8)-1)
    packet=packet<<8
    length=length&x
    packet=packet|length

    x=((1<<18)-1)
    packet=packet<<18
    data=data&x
    packet=packet|data

    x=((1<<1)-1)
    packet=packet<<1
    flag=flag&x
    packet=packet|flag

    return packet

def depacket(packet):
    x=((1<<5)-1)
    x=x<<(32-5)
    crc=(x&packet)>>(32-5)
    packet=packet&(~x)

    x=((1<<8)-1)
    x=x<<(27-8)
    length=(x&packet)>>(27-8)

    x=((1<<18)-1)
    x=x<<(19-18)
    data=(x&packet)>>(19-18)

    x=((1<<1)-1)
    x=x<<(1-1)
    flag=(x&packet)>>(1-1)
    return crc,length,data,flag

def depacket_leftshift(packet):
    x=((1<<1)-1)
    flag=packet&x
    packet=packet>>1

    x=((1<<18)-1)
    data=packet&x
    packet=packet>>18

    x=((1<<8)-1)
    length=packet&x
    packet=packet>>8

    x=((1<<5)-1)
    crc=packet&x

    return crc,length,data,flag

def main():
    crc=input("Enter crc")y
    length=input("Enter Length")
    data=input("Enter data")
    flag=input("Enter flag")

    packet=create_packet(crc,length,data,flag)
    print("Packet is {}".format(packet))

    print
    print("Depacketization:")
    crc_return,length_return,data_return,flag_return=depacket_leftshift(packet)
    
    print("Crc={}".format(crc_return))
    print("Length={}".format(length_return))
    print("Data={}".format(data_return))
    print("Flag={}".format(flag_return))

if __name__=='__main__':
    main()
