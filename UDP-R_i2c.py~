import socket
import serial 
import time
import threading
import smbus


UDP_IP = "0.0.0.0"
UDP_PORT = 5005
data = ""
#s = serial.Serial('/dev/ttyACM0' , 9600)

sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

bus = smbus.SMBus(1)

SLAVE_ADDRESS = 0x04

class Mythread(threading.Thread):

 def run(self):
	global data
	global SLAVE_ADDRESS
	while(True):
	 
        if data == "w":
	 bus.write_byte(SLAVE_ADDRESS,ord("w"))
         data = "1"

        if data == "a":
	 bus.write_byte(SLAVE_ADDRESS,ord("a"))
         data = "1"

        if data == "s":
	 bus.write_byte(SLAVE_ADDRESS,ord("s"))
         data = "1"

        if data == "d":
	 bus.write_byte(SLAVE_ADDRESS,ord("d"))
         data = "1"
	 
	time.sleep(0.0010)
	 	

mythread = Mythread()
mythread.start()

while True:
       data, addr = sock.recvfrom(10240) # buffer size is 1024 bytes
       print "received message:", data
      
