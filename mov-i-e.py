#!/usr/bin/env python
#encoding:utf-8

  # TODO use other smtp servers
  # TODO use only threading module?
  # TODO background frame timer

import smtplib
import numpy as np
import cv2
import argparse
from processing import *
from imageIterator import Iterator
from datetime import datetime
from emailHandler import EmailHandler
from repeatableTimer import RepeatableTimer
import thread


def _parse_arguments():
    # Argument and command-line options parsing
    parser = argparse.ArgumentParser(description='Webcam capture with email notification.')
    parser.add_argument('-f', '--from', metavar='email', dest='fromaddr',
                        help='sender email')
    parser.add_argument('-t', '--to', metavar='email', dest='toaddr',
                        help='destination email')
    return parser.parse_args()

def pre(img):
  """ Função de preprocessamento do iterador. """
  
  gray = toGray(img)
  filt = gaussianFilter(gray, (11,11))
  
  return filt

def main():
  args = _parse_arguments()
  notify = False
  count = 0
  if args.fromaddr:
    notify = True
    msg = raw_input("Message to send: ")
    if args.toaddr is None:
      args.toaddr = args.fromaddr
    if msg:
      eh = EmailHandler(args.fromaddr,args.toaddr,msg)
    else:
      eh = EmailHandler(args.fromaddr,args.toaddr)

  t = RepeatableTimer(60.0, eh.reset)
  # Abre stream na webcam 0
  cap = cv2.VideoCapture(0)
  capture = lambda: cap.read()[1]
  # Iterador do stream
  it = Iterator(capture, preprocess=pre)

  # Define the codec and create VideoWriter object
  fourcc = cv2.VideoWriter_fourcc(*'MJPG')
  out = cv2.VideoWriter('capture/output.avi',fourcc, 30.0, (640,480))

  print "\nPress q to quit..."
  # Loop de captura
  for i in it:
    
    frame = it.raw
    
    # Detecção de movimento (laplaciano + threshold)
    lap = laplacian(i)
    thr = threshold(lap, 200) # old 135

    # Imprime data e hora
    cv2.putText(frame, str(datetime.now()), (70,50), 0, 0.8, (50,50,50))

    # caso de mandar varios emails
    if thr.sum() > 0:

      if eh.email < 10:
        eh.inc()
      if eh.email == 10 and notify:
        eh.inc()
        cv2.imwrite('capture/screenshot%d.png' % count, frame)
        thread.start_new_thread(eh.connect,(count,))
        count += 1
        t.start()

      out.write(frame)    

      # Desenha circulo de "gravando"
      cv2.circle(frame, (40,40), 5, (10,10,255), thickness=30) 
    
    
    cv2.namedWindow("frame", cv2.WINDOW_NORMAL); 
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  # Free's
  t.cancel()
  cap.release()
  out.release()
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main()
