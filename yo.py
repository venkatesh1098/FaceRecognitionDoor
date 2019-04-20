from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import pickle
import time
import cv2
import os
import json 
import serial
import notify2

 
os.system('python3 recognize_video.py --detector face_detection_model \	                --embedding-model openface_nn4.small2.v1.t7 \
	    --recognizer output/recognizer.pickle \
	    --le output/le.pickle')