import socket
from time import sleep # for sleep

#conf. host and port
DRONE_IP = '192.168.1.1'
DRONE_PORT = 5556

CTAKEOFF = 'AT*REF=1,290718208\r' # AT command: takeoff
#CTAKEOFF = 'AT*REF=1,0b10001010101000000001000000000\r' # AT command: takeoff
CLAND    = 'AT*REF=2,290717696\r' # AT command: land

#setup UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.bind((LOCAL_IP,LOCAL_PORT))

#connect
s.connect((DRONE_IP,DRONE_PORT))

#s.getsockname()
#s.getpeername()

s.send(CTAKEOFF)
sleep(5)
s.send(CLAND)

s.close()

