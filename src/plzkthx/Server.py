'''
Created on Jan 19, 2014

@author: Zim
'''

import socket
import threading
import time

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
            (self.clientsocket, self.clientaddress) = self.serversocket.accept()
            print("hi!")
