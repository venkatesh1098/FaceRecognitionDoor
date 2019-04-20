import json
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
camera = cv2.VideoCapture(0)
i = 0
j=1
folder='/home/venkatesh/Desktop/IOT Door Security/image capture/captured/'+st
ts = time.time()
#createFolder(st)
path=(folder+'/'+st)
path=(folder+'/'+st)
if j==1:
    for i in range (10):
	    raw_input
	    return_value, image = camera.read()
	    createFolder(folder+'/'+st)
	    cv2.imwrite(path+str(i)+'.png', image)
            # i+=1
    del(camera)

# Reading data serially from Arduino
ArduinoUnoSerial = serial.Serial('/dev/ttyACM0',9600)#Setting the port for reading data
time.sleep(1)
# TO Train The Model
# os.system('python3 extract_embeddings.py --dataset dataset \
# 	--embeddings output/embeddings.pickle \
# 	--detector face_detection_model \
# 	--embedding-model openface_nn4.small2.v1.t7')
while True:
    print("************************")
    a1=ArduinoUnoSerial.readline().decode('utf-8,')
    # print(type(data))
    data = float(a1)
    if(data<=22):
        print(a1)
        data+=1
        for i in range (10):
		# raw_input
		    return_value, image = camera.read()
		    createFolder(folder+'/'+st)
		    cv2.imwrite(path+str(i)+'.png', image)
		    i+=1
        del(camera)
        # ArduinoUnoSerial.write("1")
        
        os.system('python3 recognize_video.py --detector face_detection_model \
	                --embedding-model openface_nn4.small2.v1.t7 \
	                --recognizer output/recognizer.pickle \
	                --le output/le.pickle')
        
        # snap()
        
        # ArduinoUnoSerial.write('1')
    else:
        # data=data-2
        print ("hello")
        # ArduinoUnoSerial.write('0')
