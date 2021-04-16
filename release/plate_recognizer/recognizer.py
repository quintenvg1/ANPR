##set location for the device
#database tools
locations = ("agora", "gratiekapel", "middelheim") # lijst kan worden uitgebreid
import mysql.connector as mysql
#image processing tools
import time
import cv2
import pytesseract
import os
from PIL import Image #use the pillow library
import matplotlib as plt
#serial connection tools
import serial as ser
import _thread as thread


location = "gratiekapel" #change this per location, or it won't work
result = ""
#videoCaptureObject = cv2.VideoCapture(0)
images = []
res = "" # license plate
plaat = ""
timer = 0

filterSize =(75, 75) 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filterSize)

mydb = mysql.connect(
    user = "quinten",
    password = "quintenvg1",
    host = "localhost",
    database = "ANPR",
    auth_plugin = 'mysql_native_password',
    )
#should've created a connection

try:
    arduino = ser.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=0.1)
except:
    print("the arduino is not connected, or has to be programmed first, also check port permissions")


def take10pictures():
    videoCaptureObject = cv2.VideoCapture(0)
    for i in range(10):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("pictures/picture" +str(i)+ ".jpg", frame)
    #endfor
    videoCaptureObject.release()
#end-take10pictures

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
    plates = ""
    for image in images:
        print(image)
        input_image = cv2.imread(image)
        #cv2.imshow("input image", input_image)
        #cv2.waitKey()
        input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
          
        # Applying the Black-Hat operation 
        tophat_img = cv2.morphologyEx(input_image, cv2.MORPH_BLACKHAT, kernel) 
        #cv2.imshow("original", input_image) 
        #cv2.imshow("tophat", tophat_img) 
        #cv2.waitKey()
        text = pytesseract.image_to_string(tophat_img)
        print("=================\n")
        print(image)
        print(text)
        f.write("================\n")
        f.write(image)
        f.write("\n")
        f.write(text)
        f.write("\n")
        res = text
        plates += find_in_database(res[0: (len(res) -2)])
    #endfor
    #print(plates)
    return(plates)
#end-recognize

def opengate():
    global arduino
    x = "1"
    arduino.write(bytes(x.encode("utf8")))
#end-opengate

def closegate():
    global arduino
    x = "2"
    arduino.write(bytes(x.encode("utf-8")))
#end-closegate

def find_in_database(plate):
    global mydb
    cursor = mydb.cursor()
    query = "select * from gratiekapel where nummerplaat = "+"'"+plate+"';"
    try:
        cursor.execute(query)
    except:
        print("error in the query because of random characters")
        pass
    result = ""
    for x in cursor:
        result += str(x)
    #print(result)
    return(result)
#end_find_in_database

def timerf():
    global timer
    if(timer > 0):
        timer -= 1
    if(timer == 1): # run the closegate only once
        closegate()
    #endif
    
        
#endtimer

def runtimer():
    while True:
        timerf()
        time.sleep(1)
    #endwhile
#end-runtimer
        
thread.start_new_thread(runtimer, ())

def main():
    entry = ""
    global res
    global plaat
    global timer
    #loop for this program
    print("entered program loop")
    #take a picture
    try:
        take10pictures() #only works if an optical device is connected to the system
    except:
        print("for some reason the pictures aren't coming through, check the connection")
    nummerplaten = recognize() # returns recognized plates
    
    if(nummerplaten != ""): # open the gate and set the timer to close the gate
        timer = 20
        opengate()


while True:
    while timer != 0: print("waiting")
    time.sleep(0.5) #don't overload the main thread so that other programs can keep running as well
    main() #run the main thread
#main()


