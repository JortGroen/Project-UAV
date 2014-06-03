#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Mr.Gr33n
#
# Created:     06-05-2014
# Copyright:   (c) Mr.Gr33n 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import socket
import time

#conf. host and port
DRONE_IP='192.168.1.1'
DRONE_PORT=5556

#LOCAL_IP=socket.gethostname()
#LOCAL_PORT=5556


CTAKEOFF='AT*REF=101,290718208\r' # AT command: takeoff
CLAND ='AT*REF=102,290717696\r' # AT command: land

#setup UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((DRONE_IP, DRONE_PORT))        # Bind to the port


def main():
    s.connect((DRONE_IP, DRONE_PORT))     # Connect to host at port
    #s.send(CTAKEOFF)
    #time.sleep(10)
    #s.send(CLAND)
    s.close()
if __name__ == '__main__':
    main()


