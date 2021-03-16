import cv2

videoCaptureObject = cv2.VideoCapture(0)

for i in range(10):
    ret,frame = videoCaptureObject.read()
    #cv2.imshow('Capturing Video',frame)
    cv2.imwrite("pictures/that picture" +str(i)+ ".png", frame)
videoCaptureObject.release()

