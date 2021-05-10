# Importing Libraries
import serial
import time
arduino = serial.Serial(port='/dev/ttyUSB1', baudrate=9600, timeout=0.1)
def write(x):
    arduino.write(bytes(x, 'utf-8'))

while True:
    num = input("Enter a number: ") # Taking input from user
    write(num)