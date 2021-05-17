#!/bin/bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt install python3 python3-pip tesseract-ocr tensorflow mysql phpmyadmin
sudo pip3 install wxpython mysql.connector opencv-contrib-python pytesseract imutils skimage