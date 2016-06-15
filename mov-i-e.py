#!/usr/bin/python
#encoding:utf-8

import numpy as np
import cv2
from processing import *
from imageIterator import Iterator
from datetime import datetime

# Abre stream na webcam 0
cap = cv2.VideoCapture(0)
capture = lambda: cap.read()[1]

def pre(img):
  """ Função de preprocessamento do iterador. """
  
  gray = toGray(img)
  filt = gaussianFilter(gray, (11,11))
  
  return filt

# Iterador do stream
it = Iterator(capture, preprocess=pre)

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'MJPG')
out = cv2.VideoWriter('capture/output.avi',fourcc, 30.0, (640,480))

# Loop de captura
for i in it:
  
  frame = it.raw
  
  # Detecção de movimento (laplaciano + threshold)
  lap = laplacian(i)
  thr = threshold(lap, 135)
  
  # Imprime data e hora
  cv2.putText(frame, str(datetime.now()), (70,50), 0, 0.8, (50,50,50))

  if thr.sum() > 0:
    out.write(frame)
    
    # Desenha circulo de "gravando"
    cv2.circle(frame, (40,40), 5, (10,10,255), thickness=30) 
  
  
  cv2.namedWindow("frame", cv2.WINDOW_NORMAL); 
  cv2.imshow('frame',frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
      break


# Free's
cap.release()
out.release()
cv2.destroyAllWindows()

