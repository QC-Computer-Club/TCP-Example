'''
Created on Jan 19, 2014

@author: Zim
'''
import socket
import plzkthx.Server

serv = plzkthx.Server.Server()
serv.start()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 54321))