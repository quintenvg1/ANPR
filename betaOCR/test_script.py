import cv2
import pytesseract
import os
from PIL import Image #use the pillow library
import serial
from DatabaseReader import _DatabaseReader
import tensorflow as tf

a = _DatabaseReader

res = a.select("ABC")
print(res)

#define the serial port connection
try:
    port = "/dev/ttyACM0"
    ser = serial.Serial(port, 9600)
    result = ser.readline()
    ser.write(b"test");
    print(result)
except:
    print("no device found or connected, check access rights for the port and device connection")
# Defining the kernel to be used in Top-Hat 
filterSize =(10, 10) 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filterSize)
############

filepath = "./"
images = []
for filename in os.listdir(filepath):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        images.append(filename)
        #put all the images in the array
    #endif
#endfor

#clear the log file
f = open("lastscan.txt", "w")
f.write("")
f.close()
#file should be cleared

def originalscript():
    #log all images
    f = open("lastscan.txt", "a")
    for image in images:
        image_to_edit = Image.open(image)
        image_to_edit = image_to_edit.convert("LA") #create grayscaled image
        #image_to_edit.show()
        text = pytesseract.image_to_string(image_to_edit)
        f.write("================\n")
        f.write(image)
        f.write("\n")
        f.write(text)
        f.write("\n")
        print(image)
        print(text)

    f.close()

    #print(f.readlines()) #io error on closed file
#endoriginalscript
def newscript():
    # Reading the image named 'input.jpg'
    f = open("lastscan.txt", "a")
    for image in images:
        input_image = cv2.imread(image) 
        input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
          
        # Applying the Black-Hat operation 
        tophat_img = cv2.morphologyEx(input_image, cv2.MORPH_BLACKHAT, kernel) 
        #cv2.imshow("original", input_image) 
        #cv2.imshow("tophat", tophat_img) 
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
        
#endnewscript

#originalscript()
newscript()