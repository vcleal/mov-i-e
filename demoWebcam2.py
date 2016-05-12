#!/usr/bin/python
#encoding:utf-8

import numpy as np
import cv2
import processing


if __name__ == "__main__":

  # Abre stream na webcam 0
  cap = cv2.VideoCapture(0)

  # Ultimas duas imagens
  z1 = None
  z2 = None

  # Loop de captura
  while(True):
    
    # Captura um quadro
    ret, frame = cap.read()
    
    filtered = processing.preprocess(frame)

    try:
      lap = processing.laplacian(z2, z1, filtered)
      z2 = z1
      z1 = filtered
      
    # Condição de inicialização: 3 imagens capturadas
    except TypeError:
      z2 = z1
      z1 = filtered
      continue
    
    thresh = processing.threshold(lap, 133)
    
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
