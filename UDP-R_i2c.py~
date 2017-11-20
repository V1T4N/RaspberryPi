# -*- coding: utf-8 -*-

import socket
import serial 
import time
import threading
import smbus


UDP_IP = "0.0.0.0" #IPアドレス 受信側はlocalhost
UDP_PORT = 5005 #UDPパケット送受信に使うポート
data = ""


sock = socket.socket(socket.AF_INET, 
                         socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

bus = smbus.SMBus(1) #i2c初期化

SLAVE_ADDRESS = 0x04 #i2cスレーブアドレス

class Mythread(threading.Thread): #マルチスレッド処理

 def run(self):
	global data #変数のグローバル化
	global SLAVE_ADDRESS
	while(True):
         #wasdキーでそれぞれUDPパケット受信　受信後dataを”１”にしてクリアする
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

while True: #UDP受信 
       data, addr = sock.recvfrom(1024) #バッファ1024byte
       print "received message:", data  #受信したデータを表示
      
