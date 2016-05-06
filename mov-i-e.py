#!/usr/bin/python

import numpy as np
import cv2
import time
import matplotlib.pyplot as plt

Demo = True

# Abre stream na webcam 0
cap = cv2.VideoCapture(0)

last = None

while(True):
  
  # Captura um quadro
  ret, frame = cap.read()

  # Converte frame para escala de cinza
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Filtro gaussiano 9x9
  filtered = cv2.GaussianBlur(gray, (9, 9), 0)

  try:
    # "Derivada" da imagem
    frameDelta = cv2.absdiff(last,filtered)
    last = filtered
    
  except:
    last = filtered
    continue
  
  # Threshold 10
  ret, thresh = cv2.threshold(frameDelta, 15, 255, cv2.THRESH_BINARY)
  
  # Contornos 
  im2, contours = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_TC89_L1)
  cv2.drawContours(frame, im2, -1, (0,0,255), 3)


  # Cria janela e mostra o frame
  if Demo:
    cv2.namedWindow("imagem", cv2.WINDOW_NORMAL); 
    cv2.imshow('imagem',frame)
    
    cv2.namedWindow("filtrada", cv2.WINDOW_NORMAL); 
    cv2.imshow('filtrada',filtered)
    
    cv2.namedWindow("diferencial", cv2.WINDOW_NORMAL); 
    cv2.imshow('diferencial',frameDelta)
    
    cv2.namedWindow("threshold", cv2.WINDOW_NORMAL); 
    cv2.imshow('threshold',thresh)
       
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break


cap.release()
cv2.destroyAllWindows()
