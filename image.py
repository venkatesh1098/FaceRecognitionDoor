import cv2
import os

import time
ts = time.time()

import datetime
st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')

#creating folders with timestamp
def createFolder(directory):
    try:
		
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

camera = cv2.VideoCapture(0)
i = 0
j=1
folder='/home/venkatesh/Desktop/IOT Door Security/image capture/captured/'+st
ts = time.time()
#createFolder(st)
path=(folder+'/'+st)
if j==1:
	for i in range (10):
		# raw_input
		return_value, image = camera.read()
		createFolder(folder+'/'+st)
		cv2.imwrite(path+str(i)+'.png', image)
		i+=1
	del(camera)





