#!/usr/bin/python
#encoding:utf-8

import numpy as np
import cv2
import time
import matplotlib.pyplot as plt

Demo = True

# Converte frame para escala de cinza
toGray = lambda frame: cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Filtro gaussiano 9x9
gaussianFilter = lambda img, shape: cv2.GaussianBlur(img, shape, 0)

# Laplaciano da imagem
laplacian = lambda z2, z1, z0: -z2/2 + z1 -z0/2

# "Diferença" da imagem
#frameDelta = cv2.absdiff(last,filtered)

# Deslocamento:
z = lambda array: np.roll(array,-1,axis=0)

# Threshold 15
threshold = lambda img, t: cv2.threshold(img, t, 255, cv2.THRESH_BINARY)[1]


if __name__ == "__main__":

  # Abre stream na webcam 0
  cap = cv2.VideoCapture(0)
  
  dir(cap)

  # Ultimas duas imagens
  z1 = None
  z2 = None

  while(True):
    
    # Captura um quadro
    ret, frame = cap.read()
    
    gray = toGray(frame)
    filtered = gaussianFilter(gray, (9,9))

    try:
      lap = laplacian(z2, z1, filtered)   
      z2 = z1
      z1 = filtered   
      
    # Condição de inicialização: 3 imagens capturadas  
    except TypeError:
      z2 = z1
      z1 = filtered
      continue
    
    thresh = threshold(lap, 135)
    
    # Contornos 
    im2, contours = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_NONE)


    # Cria janela e mostra o frame
    if Demo:
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
