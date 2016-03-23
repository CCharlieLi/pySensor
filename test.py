import requests, time
import sys,time,socket
from Sensor import Sensor

if __name__ == "__main__":
    sensor = Sensor("/dev/ttyUSB0",9600)
    while True:
        data = sensor.PM25_Hex(10).split(" ")
        pm = int(data[3]+data[2], 16)/10
        #print 'PM2.5:',  pm
        try:
            if socket.gethostbyname("skyrover.com.cn") == '120.25.81.22':
                r = requests.get("http://120.25.81.22:8000/idata/"+str(time.strftime("%H:%M:%S", time.localtime()))+"/"+str(pm)+"/",timeout=3)
                print(r.url, r.text)
        except Exception, e:
            print e,  ': trying to reconnect in 3 seconds...'
            time.sleep(3)
            continue;