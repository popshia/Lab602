from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import os
from ..interface_initialize.interface_with_class import *


def ReadVideo():
    video_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=(
        ("all files", "*.*"), ("MP4 files", "*.mp4 *.m4v"), ("avi files", "*.avi")))
    cap = cv2.VideoCapture(video_path)

    def DrawCanvas():
        ret, frame = cap.read()
        if (ret == True):
            print(cap.get(cv2.CAP_PROP_FPS))
            video_frame = cv2.cvtColor(cv2.resize(frame, (320, 180)), cv2.COLOR_BGR2RGB)
            img_frame = ImageTk.PhotoImage(Image.fromarray(video_frame))
            imageCanvas.create_image(0, 0, anchor=NW, image=img_frame)
            imageCanvas.img = img_frame
            imageCanvas.after(1, DrawCanvas)

    DrawCanvas()
