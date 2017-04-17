#! /usr/bin/python3
import socket
from datetime import datetime
import threading

log = open("Server.log","a+")

class Server():
    def __init__(self,usr_port=123):
        self.Socket_Object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HostName = socket.gethostname()
        self.Port = int(usr_port)
        self.Socket_Object.bind((self.HostName, self.Port))

    def Start(self):
        self.Socket_Object.listen(1)  
        print("{}  Server Started.".format(datetime.now()))
        print("{}  Server Started".format(datetime.now()), file=log)
    def Close(self):
        self.Socket_Object.shutdown(2)  # 0:disallowRecv,1:disallowSend,2:both
        self.Socket_Object.close()
        print("{}  Server Closed.".format(datetime.now()))
        print("{}  Server Closed.\n".format(datetime.now()),file=log)

class Server_Connection():
    def __init__(self,Server):
        self.conn, self.Address = Server.Socket_Object.accept()
    def Start_Connection(self):
        try:           
            print("{}  Server Connected to :{}".format(datetime.now(), self.Address))
            print("{}  Server Connected to :{}".format(datetime.now(), self.Address),file=log)
            while True:
                data_received = b''
                data_received = self.conn.recv(128)
                self.data_received = data_received.decode('ascii')
                print("\n{}  Recieved data : {} from {}".format(datetime.now(),self.data_received,self.Address))
                print("{}  Recieved data : {} from {}".format(datetime.now(),self.data_received,self.Address),file=log)
                if self.data_received == ("Q" or "EXIT" or "q" or "exit"):
                    data_send = 'Connection Closed Successfully !!'
                    self.conn.send(b'Connection Closed Successfully !!')
                    self.Close_Connection()
                else:
                    data_send = "Server Recieved mssg"
                    self.conn.send(b"Server Recieved mssg")
                print("\n{}  Send data : {} from {}".format(datetime.now(), data_send, self.Address))
                print("{} Send data : {} from {}".format(datetime.now(), data_send, self.Address), file=log)
        except:
            self.Close_Connection()
            

    def Close_Connection(self):
        self.conn.close()
        print("{}  Connection Closed from :{}".format(datetime.now(),self.Address))
        print("{}  Connection Closed from :{}".format(datetime.now(),self.Address),file=log)

class server_main():
    def __init__(self,port):
        TCP = Server(port)
        try:
            
            TCP.Start()
            while True:
                Client = Server_Connection(TCP)
                Client_thread = threading.Thread(target = Client.Start_Connection,)
                Client_thread.start()
        except:
            TCP.Close()
            log.flush()
        log.close()
