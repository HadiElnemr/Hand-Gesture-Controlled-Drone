from copy import deepcopy
import sys
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from util import *
from parameters import *


cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, minTrackCon=0.5, maxHands=1)
track = False

while True:
    output = None

    # Get image frame
    success, frame = cap.read()
    
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = 255-gray
    # find the colors within the specified BGR colour boundaries and apply the mask
    # mask = cv2.inRange(frame, lower, upper)
    
    # cv2.imshow('mask', mask)
    # cv2.imshow('255-mask', 255-mask)

    # output = cv2.bitwise_and(frame, frame, mask = 255 - mask)
    # cv2.imshow('output', output)
    # take only that specific colour
    # frame = np.hstack([frame, output])
    # frame = output

    # Find the hand and its landmarks
    hands, frame_draw_hand = detector.findHands(deepcopy(frame))  # with draw
    # hands = detector.findHands(frame, draw=False)  # without draw

    
    if hands:
        # Hand 1
        hand1 = hands[0]
        # lmList1 = hand1["lmList"]  # List of 21 Landmark points
        # bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        # centerPoint1 = hand1['center']  # center of the hand cx,cy
        # handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)
        
        if fingers1 == [1,0,0,0,0]:
            track = True
            
        if track:
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
            
    else:
        track = False
    if track:
        frame = frame_draw_hand
    cv2.imshow("Image", frame) 
    # Display
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
