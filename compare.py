#!/usr/bin/python
#encoding:utf-8

import numpy as np
import cv2
from  processing import *
from imageIterator import Iterator


# Abre stream na webcam 0
cap = cv2.VideoCapture(0)
capture = lambda : cap.read()[1]

it = Iterator(capture, preprocess=pre2)

# Loop de captura
for i in it:
  
  frame = it.raw
    
  if det2(i):
    cv2.circle(frame, (40,40), 5, (10,10,255), thickness=30) 
  
  cv2.namedWindow("imagem", cv2.WINDOW_NORMAL);
  cv2.imshow('imagem',frame)

  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


cap.release()
cv2.destroyAllWindows()
