import socket
import serial 
import time
import threading

UDP_IP = "0.0.0.0"
UDP_PORT = 5005
data = ""
s = serial.Serial('/dev/ttyACM0' , 9600)

sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT)) 

class Mythread(threading.Thread):

 def run(self):
	global data
	
	while(True):
	
	 if data == "0":
	  s.write("0")
	  data = "1"
	 
	time.sleep(0.0010)
	 	

mythread = Mythread()
mythread.start()

while True:
       data, addr = sock.recvfrom(10240) # buffer size is 1024 bytes
       print "received message:", data
      
