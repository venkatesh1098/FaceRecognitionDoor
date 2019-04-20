import pyrebase
import firebase
import os
import cv2
import datetime
import json
import serial
import time
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S').strip()
config = {
    "apiKey": "AIzaSyDYRKPloXTmITBvZvHXlrzBQ4xKjDJCteg",
    "authDomain": "pyrebase-datastorage.firebaseapp.com",
    "databaseURL": "https://pyrebase-datastorage.firebaseio.com",
    "projectId": "pyrebase-datastorage",
    "storageBucket": "pyrebase-datastorage.appspot.com",
    "messagingSenderId": "1055075434270"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
cntr = 0

#creating Folders with TimeStamp


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

# def snap():


def snap():
    camera = cv2.VideoCapture(0)
    i = 0
    j = 1
    folder = '/home/venkatesh/Desktop/IOT_Door_Security/image_capture/captured/'+st
    ts = time.time()
#createFolder(st)
    path = (folder+'/'+st)
    if j == 1:
	    for i in range(10):
		    # raw_input
		    return_value, image = camera.read()
		    createFolder(folder+'/'+st)
		    cv2.imwrite(path+str(i)+'.png', image)
            # storage.child("access/new.jpeg").put(path+".png")

            # i+=1
	    del(camera)
    storage.child("recorded/"+st+".jpeg").put(path+"5.png")


# Reading data serially from Arduino
# Setting the port for reading data
ArduinoUnoSerial = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(1)
# TO Train The Model
# os.system('python3 extract_embeddings.py --dataset dataset \
# 	--embeddings output/embeddings.pickle \
# 	--detector face_detection_model \
# 	--embedding-model openface_nn4.small2.v1.t7')
while True:
    print("************************")
    a1 = ArduinoUnoSerial.readline().decode('utf-8,')
    # print(type(data))
    # cntr=0

    data = float(a1)
    if(data <= 22):
        print(a1)
        # counter = 0

        data += 1
        cntr += 1
        print(cntr)
        if (cntr == 10):
            cntr = 0
            snap()
            os.system('python3 recognize_video.py --detector face_detection_model \
	                --embedding-model openface_nn4.small2.v1.t7 \
	                --recognizer output/recognizer.pickle \
	                --le output/le.pickle')

        # snap()
        # ArduinoUnoSerial.write("1")

        # os.system('python3 recognize_video.py --detector face_detection_model \
	    #             --embedding-model openface_nn4.small2.v1.t7 \
	    #             --recognizer output/recognizer.pickle \
	    #             --le output/le.pickle')

        # snap()

        # ArduinoUnoSerial.write('1')
    else:
        # data=data-2
        print("hello")
        # ArduinoUnoSerial.write('0')
