# Python port of matlab example given at:
# http://forum.parrot.com/ardrone/en/viewtopic.php?id=4099

# This code has not been verified
# Rufus Fraanje, p.r.fraanje@hhs.nl,  30/5/13

import socket
from time import sleep


DRONE_IP = '192.168.1.1'
AT_PORT = 5556
NAVDATA_PORT = 5554

# Creating ATCommand_PORT
ARc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Creating NAVDATA_PORT
ARn = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ARc.connect((DRONE_IP,AT_PORT))
ARn.connect((DRONE_IP,NAVDATA_PORT))

CTAKEOFF = 'AT*REF=1,290718208\r' # AT command: takeoff
#CTAKEOFF = 'AT*REF=1,0b10001010101000000001000000000\r' # AT command: takeoff
CLAND    = 'AT*REF=2,290717696\r' # AT command: land

# Sending a packet of some bytes on NAVDATA_PORT
ARn.send('1')


# Sending the request for navdata_demo on ATCommand_PORT
AR_NAV_CONFIG = 'AT*CONFIG=2,\"general:navdata_demo\",\"TRUE\"\r'
ARc.send(AR_NAV_CONFIG)
ARn.send(CTAKEOFF)
sleep(5)
ARn.send(CLAND)
# Informing the drone periodically that we still want navdata_demo
nav_data = []
for i in  range(100):
    AR_NAV_WDG = "AT*COMWDG=%d\r" %(i)
    ARc.send(AR_NAV_WDG)

    # nav_data{i} = fread(ARn, 292, 'uint8'); % Reading navigation data
    nav_data.append(ARn.recv(292))
    time.sleep(0.05)
    nav_data[i]

# Closing UDP ports
ARc.close()
ARn.close()



