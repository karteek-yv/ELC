import cv2
import pywhatkit
import keyboard
from datetime import datetime

phone_no='+9100000'
cam = cv2.VideoCapture(0) # use appropriate number if there are multiple cameras
result, image = cam.read()
cam.release()
if result:
    cv2.imwrite("test.png", image)
    # cv2.imshow("test", image)
    # cv2.waitKey(0)
    # cv2.destroyWindow("test")
    try:
        # hr = datetime.now().hour
        # mn = datetime.now().minute
        # pywhatkit.sendwhatmsg(phone_no, "Person entered!!", hr, mn+1, 10, True, 2)
        pywhatkit.sendwhatmsg_instantly(phone_no, "Person entered!!",10, True, 2)
        # keyboard.press_and_release('enter')
        # pywhatkit.sendwhats_image(phone_no, "test.png")
        # keyboard.press_and_release('enter')
        print("Successfully Sent!")
    except:
        print("An Unexpected Error!")
else:
    print("No image detected. Please! try again")
