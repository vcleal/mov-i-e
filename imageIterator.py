# encoding: utf-8

import numpy as np

class Iterator(object):
  
  capture = None
  imgBuffer = None
  preprocess = lambda x:x
  raw = None
  
  def __init__(self, capture, preprocess=lambda x:x, bufferSize=3):
    
    self.capture = capture
    self.preprocess = preprocess
    
    # Dados da imagem para inicializar o buffer
    checkFrame = preprocess(capture()) 
    bufferShape = [bufferSize] + list(checkFrame.shape)
    
    self.imgBuffer = np.zeros(bufferShape, dtype=checkFrame.dtype)
    
    # Frames de inicializaçãp
    for i in range(bufferSize):
      self.next()
    
    
  def __iter__(self):
    return self
    
    
  def next(self):
    """Carrega uma nova imagem em cada iteração. """
    
    self.imgBuffer = np.roll(self.imgBuffer,-1,axis=0)
    self.raw = self.capture()
    self.imgBuffer[0] = self.preprocess(self.raw)
    
    return self.imgBuffer


