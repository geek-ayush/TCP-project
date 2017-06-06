#! /usr/bin/python3
import socket
import threading
import logging


logger = logging.getLogger()


class Server():
    def __init__(self, usr_port=123):
        self.Socket_Object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HostName = socket.gethostname()
        self.Port = int(usr_port)
        self.Socket_Object.bind((self.HostName, self.Port))

    def Start(self):
        self.Socket_Object.listen(1)
        logger.info("Server Started.")

    def Close(self):
        self.Socket_Object.shutdown(2)  # 0:disallowRecv,1:disallowSend,2:both
        self.Socket_Object.close()
        logger.info("Server Closed.")


class Server_Connection():
    def __init__(self, Server):
        self.conn, self.Address = Server.Socket_Object.accept()

    def Start_Connection(self):
        ''' Server is connected to client
        and client can terminate the connection by sending
        "q","Q","EXIT" or "exit".
        Otherwise connection is not terminated by the server'''
        try:
            logger.info("Server Connected to :{}".format(self.Address))
            while True:
                data_received = b''
                data_received = self.conn.recv(128)
                self.data_received = data_received.decode('ascii')
                logger.info("Recieved data : {} from {}".format(self.data_received, self.Address))
                if self.data_received == ("Q" or "EXIT" or "q" or "exit"):
                    data_send = 'Connection Closed Successfully !!'
                    self.conn.send(b'Connection Closed Successfully !!')
                    self.Close_Connection()
                else:
                    data_send = "Server Recieved mssg"
                    self.conn.send(b"Server Recieved mssg")
                logger.info("Send data : {} from {}".format(data_send, self.Address))
        except Exception as problem:
            logger.debug(problem)
        except KeyboardInterrupt:
            logger.warn("Inetrrupted by Keyboard")
        finally:
            self.Close_Connection()
    def Close_Connection(self):
        self.conn.close()
        logger.info("Connection Closed from :{}".format(self.Address))


class server_main():
    def __init__(self, port):
        TCP = Server(port)
        try:
            TCP.Start()
            while True:
                # Each Client is handled by seprate threads
                Client = Server_Connection(TCP)
                Client_thread = threading.Thread(target=Client.Start_Connection)
                Client_thread.start()
        except Exception as problem_main:
            logger.debug(problem_main)
        except KeyboardInterrupt :
            logger.warn("Interrupted by Keyboard")
        except SystemExit :
            logger.info("System Exit")
        finally:
            TCP.Close()