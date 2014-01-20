'''
Created on Jan 19, 2014

@author: Zim
'''

import socket
import threading
import time

class Client(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(("localhost", 54321))
        
    def run(self):
        while True:
            s = "Thread " + str(self.x) + " running!"
            self.s.send(bytes(s,'UTF-8'))
            time.sleep(10)