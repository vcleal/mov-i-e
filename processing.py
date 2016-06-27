#!/usr/bin/python
#encoding:utf-8

import numpy as np
import cv2

### Funções de preprocessamento ###

def toGray(frame):
  return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def gaussianFilter(img, shape):
  return cv2.GaussianBlur(img, shape, 0)
  
def meanFilter(img, shape):
  return cv2.blur(img,shape)
  
def medianFilter(img, size):
  return cv2.medianBlur(img,size)
  
def normalize(img):
  return cv2.normalize(img)


### Funções de detecção ###

def imgDiff(buff):
  return cv2.absdiff(buff[-2], buff[-1])

def laplacian(buff):
  return -buff[-3]/2 + buff[-2] -buff[-1]/2

def threshold(img, t):
  return cv2.threshold(img, t, 255, cv2.THRESH_BINARY)[1]
  
  
  
### Funcões combinadas de preprocessamento e deteccao úteis ###
  
def pre1(img):
  gray = toGray(img)
  filt = gaussianFilter(gray, (11,11))
  
  return filt
  
def det1(buf):
  lap = laplacian(buf)
  thresh = threshold(lap, 139)
  
  return thresh.any()>0
  
def pre2(img):
  gray = toGray(img)
  filt = medianFilter(gray, 15)
  return img

def det2(buf):
  lap = laplacian(buf)
  thresh = threshold(lap, 160)
  
  return thresh.sum()>255*16

def pre3(img):
  img = toGray(img)
  img = cv2.Canny(img,100,200)
  img = gaussianFilter(img, (11,11))
  return img

def det3(buf):
  lap = laplacian(buf)
  return lap.sum() < 7000000



  
  
