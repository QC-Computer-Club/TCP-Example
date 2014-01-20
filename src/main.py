'''
Created on Jan 19, 2014

@author: Zim
'''

import plzkthx.Server
import plzkthx.Client

serv = plzkthx.Server.Server()
serv.start()

for i in range(0, 2):
    ct = plzkthx.Client.Client(i)
    ct.start()
