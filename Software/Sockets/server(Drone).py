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




def main():
    while(1):
        try:
            print s.recv(1024)
        except:
            time.sleep(0.5)

    s.close()                # Close the connection

if __name__ == '__main__':
    main()

