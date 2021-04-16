import tkinter as tk
from PIL import Image, ImageTk
import cv2
import os
window = tk.Tk()
window.geometry("1800x1200")
window.title("Lab602")


def image():
    video_path = tk.filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=(
        ("MP4 files", "*.mp4 *.m4v"), ("AVI files", "*.avi")))
    cap = cv2.VideoCapture(video_path)

    def video_button():
        ret, frame = cap.read()
        if (ret == True):
            video_frame = cv2.cvtColor(cv2.resize(
                frame, (530, 315)), cv2.COLOR_BGR2RGB)
            img_frame = ImageTk.PhotoImage(Image.fromarray(video_frame))
            image_canvas.create_image(0, 0, anchor=NW, image=img_frame)
            image_canvas.img = img_frame
            image_canvas.after(1, video_button)
    video_button()


# Menu Bar Items
menubar = tk.Menu(window)

loadMenu = tk.Menu(menubar)
menubar.add_cascade(label="Load Data", menu=loadMenu)
loadMenu.add_command(label="Load Video", command=image)
loadMenu.add_command(label="Load ROI and Process Lines")
loadMenu.add_command(label="Load In-Out Lines")

stabalizeMenu = tk.Menu(menubar)
menubar.add_cascade(label="Stabalization", menu=stabalizeMenu)
stabalizeMenu.add_command(label="Video Stabalization (Cross)")
stabalizeMenu.add_command(label="Video Stabalization All (Cross)")
stabalizeMenu.add_command(label="Video Stabalization (Full)")
stabalizeMenu.add_command(label="Video Stabalization All (Full)")

dataExtractMenu = tk.Menu(menubar)
menubar.add_cascade(label="Data Extraction", menu=dataExtractMenu)
dataExtractMenu.add_command(label="Trajectory Data Extraction (Full)")
dataExtractMenu.add_command(label="Trajectory Data Extraction (Cross)")
dataExtractMenu.add_command(label="Trajectoty Data Extraction (Moto)")

detectionMenu = tk.Menu(menubar)
menubar.add_cascade(label="Detection", menu=detectionMenu)
detectionMenu.add_command(label="Vehicle Detection (Faster-RCNN)")
detectionMenu.add_command(label="Motor Detection (YOLO)")

outputMenu = tk.Menu(menubar)
menubar.add_cascade(label="Output Information", menu=outputMenu)
outputMenu.add_command(label="Fill up In-Out informations")
outputMenu.add_command(label="Output Replay Video")
outputMenu.add_command(label="Output Replay Video with In-Out Lines")

viewMenu = tk.Menu(menubar)
menubar.add_cascade(label="Show", menu=viewMenu)
viewMenu.add_command(label="Original Video")
viewMenu.add_command(label="PET Conflict Heat Map")
viewMenu.add_command(label="TTC Conflict Heat Map")
viewMenu.add_command(label="Trajectory Data")
viewMenu.add_command(label="Replay")
viewMenu.add_command(label="Replay In-Out Results")

helpMenu = tk.Menu(menubar)
menubar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="Show Documentation")

sedan_val = tk.BooleanVar()
truck_val = tk.BooleanVar()
bus_val = tk.BooleanVar()
trialerHead_val = tk.BooleanVar()
cargo_val = tk.BooleanVar()
moto_val = tk.BooleanVar()
bike_val = tk.BooleanVar()
pedestrain_val = tk.BooleanVar()

sedanCheckBox = tk.Checkbutton(window, text="Sedan", variable=sedan_val, onvalue=1, offvalue=0)
sedanCheckBox.place(x=1700, y=0)
tk.Checkbutton(window, text="Truck",  variable=truck_val, onvalue=1, offvalue=0).pack()
tk.Checkbutton(window, text="Bus", variable=bus_val, onvalue=1, offvalue=0).pack()
tk.Checkbutton(window, text="Trailer Head", variable=trialerHead_val, onvalue=1, offvalue=0).pack()
tk.Checkbutton(window, text="Cargo", variable=cargo_val, onvalue=1, offvalue=0).pack()
tk.Checkbutton(window, text="Moto", variable=moto_val, onvalue=1, offvalue=0).pack()
tk.Checkbutton(window, text="Bike", variable=bike_val, onvalue=1, offvalue=0).pack()
tk.Checkbutton(window, text="Pedestrian", variable=pedestrain_val, onvalue=1, offvalue=0).pack()

image_canvas = tk.Canvas(window, bg='#000000', height=950, width=1600)
image_canvas.place(x=0, y=0)
button = tk.Button(window, text="Set ROI", width=10, height=2)
button.place(x=420, y=465)

window.config(menu=menubar)
window.mainloop()
