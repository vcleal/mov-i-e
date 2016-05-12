#!/usr/bin/python
#encoding:utf-8

import numpy as np
import cv2
from processing import *

# Abre stream na webcam 0
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):

  ret, frame = cap.read()


  if r==True:
    frame = cv2.flip(frame,0)

    # write the flipped frame
    out.write(frame)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  else:
    break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()


def getImage():
  
  img = cap.read()[1]
  img = toGray(img)
  img = gaussianFilter(img, (9,9))
  
  return img
  

