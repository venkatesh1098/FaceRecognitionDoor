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

#     camera = cv2.VideoCapture(0)
#     i = 0
#     j=1
#     folder='/home/venkatesh/Desktop/IOT Door Security/image capture/captured/'+st
#     ts = time.time()
#     #createFolder(st)
#     path=(folder+'/'+st)
#     if j==1:
# 	    for i in range (10):
# 		    raw_input
# 		    return_value, image = camera.read()
# 		    createFolder(folder+'/'+st)
# 		    cv2.imwrite(path+str(i)+'.png', image)
#             i=i+1
# 	    del(camera)



ArduinoUnoSerial = serial.Serial('/dev/ttyACM0',9600)
time.sleep(1)
while 1:
    print("********")
    raw_input= ArduinoUnoSerial.readline()
    a = int(raw_input)
    #print(type(a))
    #print(raw_input)
    if(a==1):
        print ("Someone Enterd : "+raw_input)
        snap()
        ArduinoUnoSerial.write('1')                      #send 1 to the arduino's Data code       

        # camera = cv2.VideoCapture(0)
        # i = 0
        # j=1
        # folder='/home/venkatesh/Desktop/IOT Door Security/image capture/captured/'+st
        # ts = time.time()
        # createFolder(st)
        # path=(folder+'/'+st)
        # if j==1:
	    #     for i in range (10):
		#         raw_input
		#         return_value, image = camera.read()
		#         createFolder(folder+'/'+st)
		#         cv2.imwrite(path+str(i)+'.png', image)
   		#         i+=1
	    #     del(camera)
    else:
	    print ("No One Present : "+raw_input)
    # # #         # if(raw_input==0):
            #     print("inside else if")
            # else:
            #     print("inside else if else")
print(raw_input)



