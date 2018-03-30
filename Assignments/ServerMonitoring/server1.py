import subprocess


#

def SendRecv(connection, client_address):
    try:
        print('connection from, connection is', client_address, connection)

        # Receive the data in small chunks and retransmit it
        while True:
            command= connection.recv(1024)
            output=subprocess.Popen(command,shell=True,stdout=)
    finally:
        # Clean up the connection
        connection.close()

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10004)
    sock.bind(server_address)
    sock.listen(1)
    while True:
        connection, client_address = sock.accept()
        t1 = threading.Thread(target=SendRecv, args=(connection,client_address))
        t1.start()

    


if __name__=='__main__':
    main()