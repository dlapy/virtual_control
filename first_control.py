# тестируем захват движений
import mediapipe as mp
import cv2 

cap = cv2.VideoCapture(0)

hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1, min_tracking_confidence=0.5, min_detection_confidence=0.5)


while True:
    _, img = cap.read()

    result = hands.process(img)
    print(result)
    if result.multi_hand_landmarks:
        for id, lm in enumerate( result.multi_hand_landmarks[0].landmark):
            h,w, _ = img.shape
            cx,cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx,cy), 3, (255, 0, 255))
            print(id)
            print(lm)
    cv2.imshow("Hand treaking", img)
    cv2.waitKey(1)
