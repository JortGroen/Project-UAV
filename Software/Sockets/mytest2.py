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
import time
#import cv2
import struct
import numpy as np

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Create a socket object

DRONE_IP = '192.168.1.1'
DRONE_PORT=5556

LOCAL_IP=socket.gethostname()
LOCAL_PORT=5556


CTAKEOFF='AT*REF=101,290718208\r' # AT command: takeoff
CLAND ='AT*REF=102,290717696\r' # AT command: land


##def connect():
##    s.connect((DRONE_IP, DRONE_PORT))     # Connect to host at port
##
##def disconnect():
##    s.close()                   # Close the socket when done
##
##def main():
##    connect()
##
##    s.send(CTAKEOFF)
##    #time.sleep(1)
##    s.send(CLAND)
##
##    disconnect()
##
##if __name__ == '__main__':
##    main()

s.connect((DRONE_IP, DRONE_PORT))     # Connect to host at port
s.send(CTAKEOFF)
#time.sleep(1)
s.send(CLAND)

s.close()