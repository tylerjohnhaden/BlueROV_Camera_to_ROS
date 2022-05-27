#! /bin/python3

import cv2

# terminal version: gst-launch-1.0 -e -v udpsrc port=5600 ! application/x-rtp, payload=96 ! rtph264depay ! avdec_h264 ! autovideosink
cap = cv2.VideoCapture('udpsrc port=5600 ! application/x-rtp, payload=96 ! rtph264depay ! avdec_h264 ! videoconvert ! appsink')

ret, frame = cap.read()
while ret:
    
    cv2.imshow('ROV Camera', frame)
    
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
