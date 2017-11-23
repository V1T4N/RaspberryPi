# RaspberryPi

ソケット通信を使ってロボットを制御する

## Description
UDP-R_i2c.pyとUDP-R-serial.pyが受信側

UDP.pyが送信側

~i2c.pyの方はraspberrypiのi2c通信を使って接続したArduinoに文字列でデータを投げています.

~serial.pyの方はUSBで繋いだArduinoにシリアル通信(9600bps)でデータを投げています.



## Requirement
python2.7

## Author
Yuzuki Mimura

