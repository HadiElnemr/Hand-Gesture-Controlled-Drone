import sys
from cvzone.HandTrackingModule import HandDetector
import cv2
import numpy as np
import serial
import time


# fingers configs
up = [0,1,0,0,0]
down = [0,1,1,0,0]
idle = [0,1,1,1,0]
exit = [0,0,0,0,1]

# define the black colour BGR boundaries
# For black colour
lower = [0, 0, 0]
upper = [5, 5, 5]
# For Red colour
lower = [0, 0, 0]
upper = [25, 25, 250]

# create NumPy arrays from the boundaries
lower = np.array(lower, dtype = "uint8")
upper = np.array(upper, dtype = "uint8")


cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    output = None

    # Get image frame
    success, img = cap.read()
    
    # find the colors within the specified BGR colour boundaries and apply the mask
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask = mask)

    # take only that specific colour
    # img = np.hstack([img, output])
    img = output

    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw
    
    
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)
        if fingers1 == up:
            print('Up')
        elif fingers1 == down:
            print('Down')
        elif fingers1 == idle:
            print('Idle')
        elif fingers1 == exit:
            sys.exit()
        

        #if len(hands) == 2:
            # Hand 2
        #    continue
        #    hand2 = hands[1]
        #    lmList2 = hand2["lmList"]  # List of 21 Landmark points
        #    bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
        #    centerPoint2 = hand2['center']  # center of the hand cx,cy
        #    handType2 = hand2["type"]  # Hand Type "Left" or "Right"

        #    fingers2 = detector.fingersUp(hand2)

            # Find Distance between two Landmarks. Could be same hand or different hands
            # length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)  # with draw
            # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
   
    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()