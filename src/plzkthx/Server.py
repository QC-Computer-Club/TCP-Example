'''
Created on Jan 19, 2014

@author: Zim
'''

import socket
import threading
import plzkthx.ClientThread

class Server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.hostname = "localhost"
        self.port = 54321
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind((self.hostname, self.port))
        self.serversocket.listen(5)
       
    def run(self):
        while True:
            (clientsocket, clientaddress) = self.serversocket.accept()
            ct = plzkthx.ClientThread.ClientThread(clientsocket, clientaddress)
            ct.start()