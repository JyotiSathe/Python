#WAP to read basic RTP packet and depacketize it and print respective information
#Version(V)=2 bits
#padding(P)=1 bit
#extension(X)=1 bit
#CSRC count(CC)=4 bits
#Marker(M)=1 bit
#Payload type(PT)=7 bits
#sequence number=16 bits

def depacketize(packet):
    x=((1<<16)-1)
    seq=packet&x
    packet=packet>>16

    x=((1<<7)-1)
    PT=packet&x
    packet=packet>>7

    x=((1<<1)-1)
    M=packet&x
    packet=packet>>1

    x=((1<<4)-1)
    CC=packet&x
    packet=packet>>4

    x=((1<<1)-1)
    X=packet&x
    packet=packet>>1

    x=((1<<1)-1)
    P=packet&x
    packet=packet>>1

    x=((1<<2)-1)
    V=packet&x

    return V,P,X,CC,M,PT,seq

def packetize(V,P,X,CC,M,PT,seq):
    packet=0

    x=(1<<2)-1
    V=V&x
    packet=V

    x=(1<<1)-1
    P=P&x
    packet=packet<<1
    packet=packet|P

    x=((1<<1)-1)
    X=X&x
    packet=packet<<1
    packet=packet|X

    x=((1<<4)-1)
    CC=CC&x
    packet=packet<<4
    packet=packet|CC

    x=((1<<1)-1)
    M=M&x
    packet=packet<<1
    packet=packet|M

    x=((1<<7)-1)
    PT=PT&x
    packet=packet<<7
    packet=packet|PT

    x=((1<<16)-1)
    seq=seq&x
    packet=packet<<16
    packet=packet|seq

    return packet


def main():
    V=input("Enter Version")
    P=input("Enter Padding")
    X=input("Enter Extension")
    CC=input("Enter CSRC count")
    M=input("Enter Marker")
    PT=input("Enter Payload Type")
    seq=input("Enter sequnce number")
    packet=packetize(V,P,X,CC,M,PT,seq)
    print packet
    V,P,X,CC,M,PT,seq=depacketize(packet)
    print("Version={} ".format(V))
    print("Padding={} ".format(P))
    print("Extension={} ".format(X))
    print("CSRC Count={} ".format(CC))
    print("Marker={} ".format(M))
    print("Payload Type={} ".format(PT))
    print("Sequence Number={} ".format(seq))

if __name__=='__main__':
    main()
