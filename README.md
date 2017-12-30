# mov-i-e
Application for recording videos based on movement detection (even with shitty webcams)

**Dependencies:**
- Python 2.7.x
- Numpy
- OpenCV
- Python cv2

`pip install -r requirements.txt`

**Functions:**
- demoWebcam.py (demonstrates how movement detection works using real time webcam capture)
- mov-i-e.py (records movement)
    + *Optional arguments:*
        * `-f, --from` specify sender email address
        * `-t, --to` specify recipient email address (if not informed, will consider the same as sender)

**Auxiliary Scripts:**
- processing.py (low coupling image processing techniques)
- imageIterator.py (image iterator for video processing)
- emailHandler.py (provides SMTP/email notification)

