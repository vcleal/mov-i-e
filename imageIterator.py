# encoding: utf-8

import numpy as np

class Iterator(object):

  def __init__(self, capture, preprocess=lambda x:x, bufferSize=3):
    """ Inicializa um buffer de imagens. """
    
    self.capture = capture
    self.preprocess = preprocess
    
    # Dados da imagem para inicializar o buffer
    checkFrame = preprocess(capture()) 
    
    imgShape = checkFrame.shape
    bufferShape = [bufferSize] + list(imgShape)
    
    self.imgBuffer = np.zeros(bufferShape, dtype=checkFrame.dtype)
    
    # Frames de inicializaçãp
    for i in range(bufferSize):
      self.next()
      
    
  def __iter__(self):
    return self
    
    
  def next(self):
    """ Carrega uma nova imagem em cada iteração. """
    
    self.raw = self.capture()
    
    if self.raw == None:
      raise StopIteration
      
    self.imgBuffer = np.roll(self.imgBuffer,-1,axis=0)    
    self.imgBuffer[0] = self.preprocess(self.raw)
    
    return self.imgBuffer


