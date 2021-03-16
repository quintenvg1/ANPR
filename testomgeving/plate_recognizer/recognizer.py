#database tools
locations = ("agora", "gratiekapel", "middelheim") # lijst kan worden uitgebreid
import mysql.connector as mysql
#image processing tools
import cv2
import pytesseract
import os
from PIL import Image #use the pillow library
import matplotlib as plt
#serial connection tools
import serial as ser


mydb = mysql.connect(
    user = "quinten",
    password = "quintenvg1",
    host = "localhost",
    database = "ANPR"
    )
#should've created a connection


videoCaptureObject = cv2.VideoCapture(0)
images = []
res = ""
arduino = ser.Serial("/dev/ttyUSB0", baudrate=9600, timeout=0.2) # initialize serial communication

filterSize =(10, 10) 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filterSize)

def take10pictures():
    for i in range(10):
        ret,frame = videoCaptureObject.read()
        #cv2.imshow('Capturing Video',frame)
        cv2.imwrite("pictures/picture" +str(i)+ ".jpg", frame)
    videoCaptureObject.release()


try:
    arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=0.1)
except:
    print("the arduino is not connected, or has to be programmed first")


def recognize():
    filepath = "pictures/"
    global images
    images = []
    print(os.listdir(filepath))
    for filename in os.listdir(filepath):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            print("pictures/"+filename)
            images.append("pictures/"+filename)
            #put all the images in the array
        #endif
    #endfor
    
    global res # set the global result to the recognized text
    # Reading the image named 'input.jpg'
    f = open("lastscan.txt", "a")
    for image in images:
        print(image)
        input_image = cv2.imread(image)
        #cv2.imshow("input image", input_image)
        #cv2.waitKey(0)
        input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
          
        # Applying the Black-Hat operation 
        tophat_img = cv2.morphologyEx(input_image, cv2.MORPH_BLACKHAT, kernel) 
        cv2.imshow("original", input_image) 
        cv2.imshow("tophat", tophat_img) 
        cv2.waitKey(500)
        text = pytesseract.image_to_string(tophat_img)
        print("=================\n")
        print(image)
        print(text)
        f.write("================\n")
        f.write(image)
        f.write("\n")
        f.write(text)
        f.write("\n")
        res = a.select(text) #ideally this would be only the license plate
        print(res)

def opengate():
    global arduino
    x = "1"
    arduino.write(bytes(x.encode("utf8")))

def closegate():
    global arduino
    x = "2"
    arduino.write(bytes(x.encode("utf-8")))


def main():
    #loop for this program
    print("entered program loop")
    #take a picture
    try:
        take10pictures()
    except:
        print("for some reason the pictures aren't coming through, check the connection")
    recognize() # check the images for license plates
    print(images)
    #picture = cv2.imread("pictures/picture0.jpg")
    #cv2.imshow("bruh",picture)
    #cv2.waitKey(0)
main()



