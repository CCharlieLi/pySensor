import serial
import time, os

class PM25:

    """Class for PM2.5"""
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
            self.Log("Trying to connect PM2.5 board on ...")
            self.ser.open()
        except Exception, error:
            self.Log(error)

    """Show hex"""
    def hexShow(self, byte):  
        orinialData = self.ser.read(byte)
        result = ''
        hLen = len(orinialData)  
        for i in xrange(hLen):  
            hvol = ord(orinialData[i])  
            hhex = '%02x'%hvol  
            result += hhex+' '  
        self.Log('PM2.5:'+result)
        return result

    """Function for logging output"""
    def Log(self, msg):
        print "{0} - {1}".format(time.ctime(),msg) 
