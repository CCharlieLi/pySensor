import sys,time
from PMdata import PM25

if __name__ == "__main__":

    board = PM25("/dev/cu.SLAB_USBtoUART",9600)
    while 1:
    	data = board.hexShow(10).split(" ")
    	#print data[2],data[3]
    	print 'PM2.5:',int(data[3]+data[2], 16)/10  
