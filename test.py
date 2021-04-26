from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import os
window = tk.Tk()
window.geometry("1800x1200")


def image():
    video_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=(
        ("all files", "*.*"), ("MP4 files", "*.mp4 *.m4v"), ("avi files", "*.avi")))
    cap = cv2.VideoCapture(video_path)

    def video_button():
        ret, frame = cap.read()
        if (ret == True):
            print(cap.get(cv2.CAP_PROP_FPS))
            video_frame = cv2.cvtColor(cv2.resize(frame, (320, 180)), cv2.COLOR_BGR2RGB)
            img_frame = ImageTk.PhotoImage(Image.fromarray(video_frame))
            image_canvas.create_image(0, 0, anchor=NW, image=img_frame)
            image_canvas.img = img_frame
            # 每30毫秒重置副程式
            image_canvas.after(30, video_button)
    video_button()


# 建立canvas 顯示圖片
image_canvas = tk.Canvas(window, bg='#333f50', height=800, width=1200)
image_canvas.place(x=10, y=5)
# 建立讀取讀片按鈕
button = tk.Button(window, text="引入檔案", width=10, height=2, command=image)
button.place(x=1300, y=465)
window.mainloop()
