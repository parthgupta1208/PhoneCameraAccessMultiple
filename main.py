import cv2
import numpy as np
import threading

# url = "http://192.168.184.246:8080/video"
# cap = cv2.VideoCapture(url)
# while(True):
#     camera, frame = cap.read()
#     if frame is not None:
#         cv2.imshow("Frame", frame)
#     q = cv2.waitKey(1)
#     if q==ord("q"):
#         break
# cv2.destroyAllWindows()

class camThread(threading.Thread):
    def __init__(self, camID):
        threading.Thread.__init__(self)
        self.camID = camID
    def run(self):
        camPreview(self.camID)

def camPreview(camID):
    cap = cv2.VideoCapture(camID)
    while(True):
        camera, frame = cap.read()
        if frame is not None:
            cv2.imshow("camID", frame)
        q = cv2.waitKey(1)
        if q==ord("q"):
            break
    cv2.destroyAllWindows()

# Create two threads as follows
thread1 = camThread("http://192.168.184.202:8080/video")
thread2 = camThread("http://192.168.184.246:8080/video")
thread1.start()
thread2.start()