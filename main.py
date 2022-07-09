import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import socket

# Parameters
width, height = 640, 480

# Initialize camera
cap = cv.VideoCapture(0)

# Initialize hand detector
handDetector = HandDetector(maxHands=1, detectionCon=0.8)

# Initialize communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)

while True:
    # Get the frame from the webcam
    available, img = cap.read()

    # Detect hands
    hands, img = handDetector.findHands(img)

    data = []

    if hands:
        # Get the first hand detected
        hand = hands[0]

        # Extract the landmark list
        lmList = hand['lmList']

        for lm in lmList:
            data.extend([lm[0], height - lm[1], lm[2]])
        print(data)
        sock.sendto(str.encode(str(data)), serverAddressPort)

    # Output
    cv.imshow("Image", img)
    cv.waitKey(1)

