import serial
import cv2
import pywhatkit
from datetime import datetime
import pyautogui,time

phone_no='+919398781682' #use your whatsapp number

while True:
    ser = serial.Serial('/dev/ttyACM0', 9600)
    value = int(float(ser.read()))
    if value:
        print("Possible intruder\n")
        cam = cv2.VideoCapture(0) # use appropriate number if there are multiple cameras
        result, image = cam.read()
        cam.release()
        if result:
            cv2.imwrite("test.jpg", image)
            pywhatkit.sendwhats_image(phone_no, "test.jpg", "Intruder image")
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'w')
            print("Successfully Sent!")
        else:
            print("No image detected. Please! try again")
    else:
        print("Monitoring for intruder\n")
