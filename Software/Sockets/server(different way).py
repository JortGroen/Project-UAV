#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Mr.Gr33n
#
# Created:     01-05-2014
# Copyright:   (c) Mr.Gr33n 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import socket               # Import socket module
import cv2
import struct
import numpy as np
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   # Create a socket object
host = socket.gethostname() # Get local machine name (or IP)
port = 5556                # Reserve a port for your service.

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection (5 clients allowed
                        # before they are accepted)
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr

def disconnect(c):
    c.close()                # Close the connection

def send(message):
    c.send(message)

def recieve():
    data=c.recv(1024)
    if(len(data)>0):
        print(data)


def main():
    while(1):
        try:
            recieve()
        except:
            pass
        time.sleep(0.5)


if __name__ == '__main__':
    main()

