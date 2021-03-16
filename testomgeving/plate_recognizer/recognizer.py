#database tools
locations = ("agora", "gratiekapel", "middelheim") # lijst kan worden uitgebreid
import mysql.connector as mysql

mydb = mysql.connect(
    user = "quinten",
    password = "quintenvg1",
    host = "localhost",
    database = "ANPR"
    )
#should've created a connection

#image processing tools
import cv2
import pytesseract
import os
from PIL import Image #use the pillow library
import matplotlib as plt

videoCaptureObject = cv2.VideoCapture(0)
images = []
def take10pictures():
    for i in range(10):
        ret,frame = videoCaptureObject.read()
        #cv2.imshow('Capturing Video',frame)
        cv2.imwrite("pictures/picture" +str(i)+ ".jpg", frame)
    videoCaptureObject.release()

def update_images():
    filepath = "pictures/"
    global images
    images = []
    print(os.listdir(filepath))
    for filename in os.listdir(filepath):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            images.append(filename)
            #put all the images in the array
        #endif
    #endfor

def detectplates():
    global images
    for image in images:
        pic = cv2.imread(image)
        cv2.imshow(pic)
        cv2.waitKey()
        
        
#hardware control tools #change default usb port for arduino if it is on a different port

import serial

try:
    arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=0.1)
except:
    print("the arduino is not connected, or has to be programmed first")
def write(x):
    arduino.write(bytes(x, 'utf-8'))


def main():
    #loop for this program
    print("entered program loop")
    #take a picture
    take10pictures()
    update_images()
    detectplates()
    print(images)
    #cv2.imshow("bruh",picture)
    #cv2.waitKey()
    
main()



