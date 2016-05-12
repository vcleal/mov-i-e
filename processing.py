#!/usr/bin/python
#encoding:utf-8

import numpy as np
import cv2

### Conversão ###

def toGray(frame):
  """ Converte frame para escala de cinza. """
  return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


### Filtragem ###

def threshold(img, t):
  return cv2.threshold(img, t, 255, cv2.THRESH_BINARY)[1]

def gaussianFilter(img, shape):
  return cv2.GaussianBlur(img, shape, 0)
  
def laplacian(buff):
  return -buff[-3]/2 + buff[-2] -buff[-1]/2

def imgDiff(im1, im2):
  return cv2.absdiff(im0,im1)


