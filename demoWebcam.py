#!/usr/bin/python
#encoding:utf-8

import numpy as np
import cv2
from  processing import *
from imageIterator import Iterator


# Abre stream na webcam 0
cap = cv2.VideoCapture(0)
capture = lambda : cap.read()[1]

# Preprocessamento (escala de cinza e filtro gaussiano)
pre = lambda img: gaussianFilter(toGray(img), (11,11))

# Iterador do stream
it = Iterator(capture, preprocess=pre)


if __name__ == "__main__":
  
  # Loop de captura
  for i in it:
    
    frame = it.raw
    filtered = i[-1]
    lap = laplacian(i)
    thresh = threshold(lap, 135)
    
    # Contornos 
    im2, contours = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, im2, -1, (0,255,0), 3)
    
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
