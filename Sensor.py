import serial
import time, os

class Sensor:
    """Class for sensor"""
    def __init__(self, serPort, baudRate):

        self.ser = serial.Serial()
        self.ser.port = serPort
        self.ser.baudrate = baudRate
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.xonxoff = False
        self.ser.rtscts = False
        self.ser.dsrdtr = False

        self.ser.timeout = 2
        self.ser.writeTimeout = 2

        try:
            self.Log("Trying to connect sensor ...")
            self.ser.open()
        except Exception, error:
            self.Log(error)

    """Show hex"""
    def PM25_Hex(self, byte=10):  
        orinialData = self.ser.read(byte)
        result = ''
        hLen = len(orinialData)  
        for i in xrange(hLen):  
            hvol = ord(orinialData[i])  
            hhex = '%02x'%hvol  
            result += hhex+' '  
        #self.Log('PM2.5:'+result)
        return result

    def TempHumi(self):
        #length = self.ser.inWaiting()
        #if length != 0:
        #    print '--',length
        orinialData = self.ser.read(47)
        print '-',orinialData.find('\n')

    """Function for logging output"""
    def Log(self, msg):
        print "{0} - {1}".format(time.ctime(),msg) 
