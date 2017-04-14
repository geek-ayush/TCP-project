import socket
from datetime import datetime


class Server():
    def __init__(self):
        self.Socket_Object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HostName = socket.gethostname()
        self.Port = 12345
        self.Socket_Object.bind((self.HostName, self.Port))

    def Start(self):
        self.Socket_Object.listen(5)   # at max 5 connections
        print("Server Started at :#{}".format(datetime.now()))

    def Close(self):
        self.Socket_Object.shutdown(2)  # 0:disallowRecv,1:disallowSend,2:both
        self.Socket_Object.close()
        print("Server Closed at :#{}".format(datetime.now()))


class Server_Connection():
    def __init__(self):
        self.buffersize = 128   # 1024 commonly used but for faster response

    def Start_Connection(self, Server):
        try:
            self.time_start = datetime.now()
            self.conn, self.Address = Server.Socket_Object.accept()
            print("Server Connected to :", self.Address)
            data_received = b''
            while True:                
                data_received = self.conn.recv(128)
                self.data_received = data_received.decode('ascii')
                print("\n Recieved data : #{} at #{}".format(self.data_received,datetime.now()))
                if self.data_received != (b"Q" or b"EXIT"):
                    self.conn.send(b"Connection Closed Successfully !!")
                    self.Close_Connection()
                self.send(b"Server Recieved mssg")
        except:
            self.Close_Connection()
            self.time_end = datetime.now()


    def Close_Connection(self):
        self.conn.close()
        print("Server Connection has been Closed.")


s = Server()
s.Start()
st = Server_Connection()
st.Start_Connection(s)
