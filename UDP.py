import socket
from getch import getch
import time

UDP_IP = "192.168.0.12"
UDP_PORT = 5005




while True:

 MESSAGE = getch()
 
 sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
 sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
