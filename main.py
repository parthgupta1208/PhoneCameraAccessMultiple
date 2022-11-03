import cv2
import numpy as np
import threading
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

class GUIThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global root,l1,l11
        root = Tk()
        l1=Label(root)
        l1.grid(row=0,column=0)
        l11=Label(root)
        l11.grid(row=0,column=1)
        l2=Label(root,text="Camera 1")
        l2.grid(row=1,column=0)
        l22=Label(root,text="Camera 2")
        l22.grid(row=1,column=1)
        root.mainloop()

class camThread(threading.Thread):
    def __init__(self, previewName, camID,n):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
        self.n=n
    def run(self):
        print ("Starting " + self.previewName)
        if self.n==0:
            camPreview(self.camID)
        else:
            camPreview2(self.camID)

def camPreview(camID):
    cam = cv2.VideoCapture(camID)
    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False
    while rval:
        cv2image= cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGB)
        im = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=im) 
        l1.config(image=imgtk)
        l1.image=imgtk
        rval, frame = cam.read()
        key = cv2.waitKey(20)
        if key == 27:
            break

def camPreview2(camID):
    cam = cv2.VideoCapture(camID)
    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False
    while rval:
        cv2image= cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGB)
        im = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=im) 
        l11.config(image=imgtk)
        l11.image=imgtk
        rval, frame = cam.read()
        key = cv2.waitKey(20)
        if key == 27:
            break

thread0 = GUIThread()
thread1 = camThread("Cam1",0,0)
thread2 = camThread("Cam2","http://192.168.184.246:8080/video",1)
thread0.start()
thread1.start()
thread2.start()