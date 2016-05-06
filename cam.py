import numpy as np
import cv2
import time
from matplotlib import pyplot as plt

# Diff noise: pseudomovement produced by noise
DIF_NOISE = 4000

# "Hold on" detection time
DET_TIME = 1.0

# Open webcam 0
cap = cv2.VideoCapture(0)

detectTime = time.time()

def diffImg(t0, t1, t2):
  """ Generate differential image. """
  
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)

  return cv2.bitwise_and(d1, d2)


lq=0
t=0 
t_plus=0

while(True):
  
  # Capture frame-by-frame
  ret, frame = cap.read()

  # Our operations on the frame come here
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
  # Read next image
  t_minus = t
  t = t_plus
  t_plus = gray
  
  d = diffImg(t_minus, t, t_plus) 
  s = np.sum(d)
  
  
# Display the resulting frame
  
  if s > lq+DIF_NOISE:
    detectTime = time.time()

  if time.time() < detectTime + DET_TIME:
    cv2.circle(frame,(40,40), 5, (10,10,255), thickness=30) 
    
    print s, time.time() 
  
  lq = s 
  cv2.namedWindow("frame", cv2.WINDOW_NORMAL); 
  cv2.imshow('frame', frame)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

  if cv2.waitKey(1) & 0xFF == ord('c'):
    cv2.imwrite('capture/%s.png' % time.time() , frame)
    plt.imshow(frame)
    plt.plot()


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
