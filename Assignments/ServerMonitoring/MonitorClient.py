import threading
import socket

class MonitorClient(threading.Thread):
    def __init__(self,dict1):
        threading.Thread.__init__(self)
        self.ip=dict1["ip"]
        self.port=dict1["port"]
        self.status_command=dict1["status_command"]
        self.output_file=dict1["output_file"]
        self.periodic=dict1["periodic"]
        self.period=dict1["period"]

    def run(self):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_address=(self.ip,self.port)
        sock.connect(server_address)
        fd=open(self.output_file,"w")
        try:
            count=0
            while(count!=self.periodic):
                #sock.send(bytes(self.status_command,'UTF-8'))
                sock.sendall(self.status_command)
                while True:
                    data=sock.recv(10)
                    if():
                        break
                    fd.write(data)
                count+=1
                time.sleep(self.period)
        
        except:


        '''print self.ip
        print self.port
        print self.status_command
        print self.output_file
        print self.periodic
        print self.period'''

