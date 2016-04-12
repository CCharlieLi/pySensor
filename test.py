import requests, time
import sys,time,socket
from Sensor import Sensor

if __name__ == "__main__":
    sensor = Sensor("/dev/ttyUSB0",9600)
    while True:
        data = sensor.PM25_Hex(10).split(" ")
        pm = int(data[3]+data[2], 16)/10
        print 'PM2.5:',  pm
