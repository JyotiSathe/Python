import socket
import threading

def performAdd(connection, client_address):
    try:
        print('connection from, connection is', client_address, connection)
        while True:
            data=connection.recv(10)
            print data
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()

def main():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address=('localhost',10045)
    print('starting up on %s port %s'%server_address)
    sock.bind(server_address)
    sock.listen(3)
    while True:
        print("Waiting for connection")
        connection,client_address=sock.accept()
        t1=threading.Thread(target=performAdd,args=(connection,client_address))
        t1.start()
    

if __name__=='__main__':
    main()
