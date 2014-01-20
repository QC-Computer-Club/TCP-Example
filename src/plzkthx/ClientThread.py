'''
Created on Jan 19, 2014

@author: Zim
'''

import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, clientSocket, clientAdress):
        threading.Thread.__init__(self)
        self.socket = clientSocket
        self.address = clientAdress
        
    def run(self):
        while True:
            data = self.socket.recv(1024)
            print(data.decode())