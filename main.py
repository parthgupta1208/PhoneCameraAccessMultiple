import cv2
import numpy as np
import threading
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

def back():
    root.destroy()
    win.deiconify()

class GUIThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global root,l1,l11
        win.withdraw()
        root = Toplevel(win)
        l1=Label(root)
        l1.grid(row=0,column=0,padx=(30,5),pady=20)
        l11=Label(root)
        l11.grid(row=0,column=1,padx=(5,30),pady=20)
        l2=Label(root,text="Device at "+ent1.get(),font="helvetica 12")
        l2.grid(row=1,column=0)
        l22=Label(root,text="Device at "+ent2.get(),font="helvetica 12")
        l22.grid(row=1,column=1)
        b1=Button(root,text="Back",command=back)
        b1.grid(row=2,column=0,pady=(10,30),padx=(70,35),sticky="news")
        b2=Button(root,text="Exit",command=exit)
        b2.grid(row=2,column=1,pady=(10,30),padx=(35,70),sticky="news")
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

def everything():
    global ent1,ent2,s1,s2
    s1="http://"+str(ent1.get())+"/video"
    s2="http://"+str(ent2.get())+"/video"
    thread0 = GUIThread()
    thread1 = camThread("cam1",s2,0)
    thread2 = camThread("cam2",s2,1)
    thread0.start()
    thread1.start()
    thread2.start()

win=Tk()
lab1=Label(win,text="Connect Phones",font="helvetica 18 bold")
lab1.grid(row=0,column=0,columnspan=5,pady=(30,10),padx=50)
lab2=Label(win,text="Step 1 : Download \'IP-Webcam\' on both phones.\nStep 2 : Connect the phones and PC on the same network.\nStep 3 : Open IP Webcam on both phones and Start Server.\nStep 4 : Enter the IP Generated on both phones in the Text Box below and Press Continue.")
lab2.grid(row=1,column=0,columnspan=5,pady=(10,30),padx=50)
lab3=Label(win,text="Device 1 IP-Address")
lab4=Label(win,text="Device 2 IP-Address")
lab3.grid(row=2,column=0,columnspan=2)
lab4.grid(row=3,column=0,pady=(20,20),columnspan=2)
ent1=Entry(win)
ent1.grid(row=2,column=2,sticky="news",columnspan=3,padx=(10,70))
ent2=Entry(win)
ent2.grid(row=3,column=2,sticky="news",pady=(20,20),columnspan=3,padx=(10,70))
but1=Button(win,text="Continue",command=everything)
but1.grid(row=4,column=0,columnspan=3,pady=(10,30),padx=(50,80),sticky="news")
but2=Button(win,text="Exit",command=exit)
but2.grid(row=4,column=2,columnspan=3,pady=(10,30),padx=(80,50),sticky="news")
win.bind('<Return>',lambda event:everything())
win.mainloop()