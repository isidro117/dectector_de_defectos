from tkinter import *
from PIL import Image, ImageTk
import cv2
import imutils
from index import *


cap = None

def video_stream():
    global cap
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    visualizar()

def detener():
    global cap
    cap.release()

def visualizar():
    global cap
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width=320)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, visualizar)
        else:
            lblVideo.image = ""
            cap.release()


video_stream()


ventana.mainloop()