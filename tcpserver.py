import socket
from datetime import datetime

class Server():
    def __init__(self):
        self.Socket_Object = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.HostName = socket.gethostname()
        self.Port = 12345
        self.Socket_Object.bind((self.HostName,self.Port))

    def Start(self): 
        self.Socket_Object.listen(5) #at max 5 connections
        print("Server Started at :  #{}".format(datetime.now()))
    def Close(self):
        self.Socket_Object.shutdown(2)       # 0 : recieves are diallowed , 1: sends are disallowed , 2: both are disallowed
        self.Socket_Object.close()
        print("Server Closed at :   #{}".format(datetime.now()))

class Server_Connection():
    def __init__(self):
            self.buffersize = 128 #1024 commonly used but for faster response
            self.conn = None
    def Start_Connection(self,server):
        try:
            self.time_start = datetime.now()
            while True:
                self.conn , self.Address = Server.Socket_Object.accept()
                self.conn.data_received ,self.conn.ip = self.conn.recvfrom()
                print("\n Recieved data : ",self.conn.data_received)
                if self.conn.data_received.upper() != ("Q" or "EXIT") :
                    self.conn.send("Connection Closed Successfully !!")
                    self.conn.close()
                    self.sendto(32,self.conn.ip)
        except:
            self.conn.close()
            sel.time_end = datetime.now() 

    def Close_Connection(self):
        self.conn.close()

s = Server()
s.Start()
s.Close()

