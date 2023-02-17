import cv2
import mediapipe as mp
import pyautogui as pag
from sound import Sound
import time

cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(static_image_mode= False, max_num_hands = 1, min_tracking_confidence=0.1,min_detection_confidence=0.1)
widthScreen, heightScreen = pag.size()
dsize = (widthScreen,heightScreen)
volSound = Sound.current_volume()
print(volSound)
x4pos = 0
x5pos = 0
x16pos = 0
x20pos = 0
x13pos = 0
x17pos = 0
x12pos = 0
x9pos = 0
click = False
click2 = False
timer = 100
while True:
    _, img = cap.read()
    result = hands.process(cv2.resize(cv2.flip(img, 1), dsize))
    if result.multi_hand_landmarks:
        for id, lm in enumerate(result.multi_hand_landmarks[0].landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 4, (255, 255, 255))
            if id == 4:
                x4pos = cx
            if id == 5:
                x5pos = cx
            if id == 16:
                x16pos = cy
            if id == 20:
                x20pos = cy
            if id == 13:
                x13pos = cy
            if id == 17:
                x17pos = cy
            if id == 12:
                x12pos = cy
            if id == 19:
                x9pos = cy
            if x16pos > x13pos and x12pos > x9pos and x20pos > x17pos and click2 == False:
                pag.doubleClick()
                click2 = True
            elif x16pos > x13pos and x20pos > x17pos:
                timer -= 8
                if timer < 0:
                    Sound.volume_down()
                    timer = 100
            elif x16pos > x13pos and x12pos > x9pos:
                timer -= 8
                if timer < 0:
                    Sound.volume_up()
                    timer = 100
            elif x5pos < x4pos and click == False:
                click = True
                print("Нажал")
                pag.mouseDown()
            if id == 8:
                pag.moveTo(cx * widthScreen / w, cy * heightScreen / h)

            elif x5pos > x4pos and click == True:
                print("Отжал")
                pag.mouseUp()
                click = False
            else:
                click2 = False
    cv2.imshow("Hand tracking", img)
    cv2.waitKey(1)

