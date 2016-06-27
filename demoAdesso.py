#!/usr/bin/python
#encoding:utf-8

import numpy as np
import cv2
from  processing import *
from imageIterator import Iterator


# Define função adshow fora da adessowiki
if "adshow" not in dir():
  def adshow(img, name):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, img)

# Abre stream na URL
cap = cv2.VideoCapture("http://adessowiki.fee.unicamp.br/media/Attachments/courseEA9791s2016/Projeto9/output.avi")
capture = lambda : cap.read()[1]

def pre(img):
  """ Função de preprocessamento do iterador. """
  
  gray = toGray(img)
  filt = gaussianFilter(gray, (11,11))
  
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
  
  adshow(frame, 'imagem')
  adshow(filtered,'filtrada')
  adshow(lap, 'diferencial')
  adshow(thresh, 'threshold')
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


cap.release()
cv2.destroyAllWindows()
