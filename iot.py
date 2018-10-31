import serial
import time
ts = time.time()
import datetime
st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
import cv2
import os

#creating Folders with TimeStamp
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

# def snap():
def snap():
    camera = cv2.VideoCapture(0)
    i = 0
    j=1
    folder='/home/venkatesh/Desktop/IOT Door Security/image capture/captured/'+st
    ts = time.time()
#createFolder(st)
    path=(folder+'/'+st)
    if j==1:
	    for i in range (10):
		    raw_input
		    return_value, image = camera.read()
		    createFolder(folder+'/'+st)
		    cv2.imwrite(path+str(i)+'.png', image)
   		    i+=1
	    del(camera)

# Reading data serially from Arduino
ArduinoUnoSerial = serial.Serial('/dev/ttyACM1',9600)#Setting the port for reading data
time.sleep(1)
while True:
    print("************************")
    a1=ArduinoUnoSerial.readline()
    # data = int(a)
    a=1
    if(a==1):
        snap()
        a+=1
        ArduinoUnoSerial.write('1')
    else:
        ArduinoUnoSerial.write('0')

