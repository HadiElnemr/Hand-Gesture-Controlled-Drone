import sys
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from util import *
from parameters import *


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
            write_esp(1)
            print('Up')
        elif fingers1 == down:
            write_esp(-1)
            print('Down')
        elif fingers1 == idle:
            write_esp(0)
            print('Idle')
        elif fingers1 == exit:
            sys.exit()
        
    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
