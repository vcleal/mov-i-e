#!/usr/bin/python
#encoding:utf-8

import numpy as np
import cv2
from  processing import *
from imageIterator import Iterator


# Abre stream na webcam 0
cap = cv2.VideoCapture(0)
capture = lambda : cap.read()[1]

def pre(img):
  """ Função de preprocessamento do iterador. """
  
  gray = toGray(img)
  filt = medianFilter(gray, 11)
  
  return filt

# Iterador do stream
it = Iterator(capture, preprocess=pre)

# Loop de captura
for i in it:
  
  frame = it.raw
  filtered = i[-1]
  lap = laplacian(i)
  thresh = threshold(lap, 139)
  
  # Destaca regiões com movimento
  frame[thresh>0]=(0,255,0) 
  
  cv2.namedWindow("imagem", cv2.WINDOW_NORMAL);
  cv2.imshow('imagem',frame)
  
  cv2.namedWindow("filtrada", cv2.WINDOW_NORMAL);
  cv2.imshow('filtrada',filtered)
  
  cv2.namedWindow("diferencial", cv2.WINDOW_NORMAL);
  cv2.imshow('diferencial',lap)
  
  cv2.namedWindow("threshold", cv2.WINDOW_NORMAL);
  cv2.imshow('threshold',thresh)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


cap.release()
cv2.destroyAllWindows()
