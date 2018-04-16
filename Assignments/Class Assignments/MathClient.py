
import socket
def getAddition(sock,server_address,n1,n2):
    sock.connect(server_address)
    try:
        message=str(n1)+"#"+str(n2)
        print('sending "%s"' % message)
        while 1:
            #sock.send(bytes(message, 'UTF-8')) # 3 & above
            sock.sendall(message) # 2.7
            data = sock.recv(10)
            print('received "%s"' % data)
            message = input("Do you want to continue")
    finally:
        print('closing socket')
        sock.close()
        
def main():
    n1=input("Enter first number")
    n2=input("Enter second number")
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address=('localhost',10045)
    getAddition(sock,server_address,n1,n2)

if __name__=='__main__':
    main()
