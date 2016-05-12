#!/usr/bin/python
#encoding:utf-8

import numpy as np
import cv2
from processing import *
from imageIterator import Iterator

# Abre stream na webcam 0
cap = cv2.VideoCapture(0)
capture = lambda : cap.read()[1]

# Preprocessamento (escala de cinza e filtro gaussiano)
pre = lambda img: gaussianFilter(toGray(img), (11,11))

# Iterador do stream
it = Iterator(capture, preprocess=pre)

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'MJPG')
out = cv2.VideoWriter('capture/output.avi',fourcc, 30.0, (640,480))


if __name__ == "__main__":
  
  # Loop de captura
  for i in it:
    
    frame = it.raw
    lap = laplacian(i)
    thr = threshold(lap, 135)

    if thr.sum() > 0:
      out.write(frame)
      cv2.circle(frame,(40,40), 5, (10,10,255), thickness=30) 
      
    cv2.namedWindow("frame", cv2.WINDOW_NORMAL); 
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

  # Release everything if job is finished
  cap.release()
  out.release()
  cv2.destroyAllWindows()

