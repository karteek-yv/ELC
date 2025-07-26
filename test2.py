import cv2
import pywhatkit
from datetime import datetime
import pyautogui,time

phone_no='+919398781682' #use your whatsapp number
cam = cv2.VideoCapture(0) # use appropriate number if there are multiple cameras
result, image = cam.read()
cam.release()
if result:
    cv2.imwrite("test.jpg", image)
    # cv2.imshow("test", image)
    # cv2.waitKey(0)
    # cv2.destroyWindow("test")
    # hr = datetime.now().hour
    # mn = datetime.now().minute
    # pywhatkit.sendwhatmsg(phone_no, "Person entered!!", hr, mn+1, 10, True, 2)
    # pywhatkit.sendwhatmsg_instantly(phone_no, "Person entered!!",10, True, 2)
    pywhatkit.sendwhats_image(phone_no, "test.jpg", "Intruder image")
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'w')
    print("Successfully Sent!")
else:
    print("No image detected. Please! try again")
