import tkinter as tk
from tkinter import LabelFrame, font, ttk, BOTH, W, N, E, S
from PIL import Image, ImageTk
import cv2
import os
from ..menubar_functions import video_read


class Main_Window(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.init_menu_bar()
        self.init_checkbox()
        self.init_video_canvas()
        self.init_informations()

    def init_UI(self):
        self.master.title("Lab602")
        self.pack(fill=BOTH, expand=True)
        self.columnconfigure(8, weight=1)
        self.columnconfigure(9, pad=5)
        self.rowconfigure(10, weight=1)
        self.rowconfigure(13, pad=5)

    def init_menu_bar(self):
        menubar = tk.Menu(self)
        self.master.configure(menu=menubar)
        # sub menu loadmenu
        loadMenu = tk.Menu(menubar)
        menubar.add_cascade(label="Load Data", menu=loadMenu)
        loadMenu.add_command(label="Load Video", command=video_read.ReadVideo)
        loadMenu.add_command(label="Load ROI and Process Lines")
        loadMenu.add_command(label="Load In-Out Lines")
        # sub menu setMenu
        setMenu = tk.Menu(menubar)
        menubar.add_cascade(label="Set Data", menu=setMenu)
        setMenu.add_command(label="Set ROI")
        setMenu.add_command(label="Set Process Lines")
        setMenu.add_command(label="Set In-Out Lines")
        # sub menu stabalization
        stabalizeMenu = tk.Menu(menubar)
        menubar.add_cascade(label="Stabalization", menu=stabalizeMenu)
        stabalizeMenu.add_command(label="Video Stabalization (Cross)")
        stabalizeMenu.add_command(label="Video Stabalization All (Cross)")
        stabalizeMenu.add_command(label="Video Stabalization (Full)")
        stabalizeMenu.add_command(label="Video Stabalization All (Full)")
        # sub menu data extraction
        dataExtractMenu = tk.Menu(menubar)
        menubar.add_cascade(label="Data Extraction", menu=dataExtractMenu)
        dataExtractMenu.add_command(label="Trajectory Data Extraction (Full)")
        dataExtractMenu.add_command(label="Trajectory Data Extraction (Cross)")
        dataExtractMenu.add_command(label="Trajectoty Data Extraction (Moto)")
        # sub menu detection
        detectionMenu = tk.Menu(menubar)
        menubar.add_cascade(label="Detection", menu=detectionMenu)
        detectionMenu.add_command(label="Vehicle Detection (Faster-RCNN)")
        detectionMenu.add_command(label="Motor Detection (YOLO)")
        # sub menu output information
        outputMenu = tk.Menu(menubar)
        menubar.add_cascade(label="Output Information", menu=outputMenu)
        outputMenu.add_command(label="Fill up In-Out informations")
        outputMenu.add_command(label="Output Replay Video")
        outputMenu.add_command(label="Output Replay Video with In-Out Lines")
        # sub menu show
        viewMenu = tk.Menu(menubar)
        menubar.add_cascade(label="Show", menu=viewMenu)
        viewMenu.add_command(label="Original Video")
        viewMenu.add_command(label="PET Conflict Heat Map")
        viewMenu.add_command(label="TTC Conflict Heat Map")
        viewMenu.add_command(label="Trajectory Data")
        viewMenu.add_command(label="Replay")
        viewMenu.add_command(label="Replay In-Out Results")
        # sub menu help
        helpMenu = tk.Menu(menubar)
        menubar.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="Show Documentation")

    def init_checkbox(self):
        # check box booleans
        sedanCheckBoxBool = tk.BooleanVar()
        truckCheckBoxBool = tk.BooleanVar()
        busCheckBoxBool = tk.BooleanVar()
        trailerCheckBoxBool = tk.BooleanVar()
        cargoCheckBoxBool = tk.BooleanVar()
        motoCheckBoxBool = tk.BooleanVar()
        bikeCheckBoxBool = tk.BooleanVar()
        pedestrainCheckBoxBool = tk.BooleanVar()
        # check box attributes ( font, labelFrame )
        checkBoxFont = font.Font(size=20)
        checkBoxFrame = LabelFrame(self, text='Check Boxes', font=checkBoxFont)
        checkBoxFrame.grid(column=9, row=2, sticky=E+W+S+N, padx=10)
        # sedan checkbox
        sedanCheckBox = tk.Checkbutton(checkBoxFrame, text="Sedan", variable=sedanCheckBoxBool,
                                       onvalue=1, offvalue=0, font=checkBoxFont)
        sedanCheckBox.grid(column=1, row=1, sticky=W, padx=5, pady=5)
        # truck checkbox
        truckCheckBox = tk.Checkbutton(checkBoxFrame, text="Truck",  variable=truckCheckBoxBool,
                                       onvalue=1, offvalue=0, font=checkBoxFont)
        truckCheckBox.grid(column=1, row=2, sticky=W, padx=5, pady=5)
        # bus checkbox
        busCheckBox = tk.Checkbutton(checkBoxFrame, text="Bus", variable=busCheckBoxBool,
                                     onvalue=1, offvalue=0, font=checkBoxFont)
        busCheckBox.grid(column=1, row=3, sticky=W, padx=5, pady=5)
        # trailer checkbox
        trailerCheckBox = tk.Checkbutton(checkBoxFrame, text="Trailer Head", variable=trailerCheckBoxBool,
                                         onvalue=1, offvalue=0, font=checkBoxFont)
        trailerCheckBox.grid(column=1, row=4, sticky=W, padx=5, pady=5)
        # cargo checkbox
        cargoCheckBox = tk.Checkbutton(checkBoxFrame, text="Cargo", variable=cargoCheckBoxBool,
                                       onvalue=1, offvalue=0, font=checkBoxFont)
        cargoCheckBox.grid(column=1, row=5, sticky=W, padx=5, pady=5)
        # moto chcekbox
        motoCheckBox = tk.Checkbutton(checkBoxFrame, text="Moto", variable=motoCheckBoxBool,
                                      onvalue=1, offvalue=0, font=checkBoxFont)
        motoCheckBox.grid(column=1, row=6, sticky=W, padx=5, pady=5)
        # bike checkbox
        bikeCheckBox = tk.Checkbutton(checkBoxFrame, text="Bike", variable=bikeCheckBoxBool,
                                      onvalue=1, offvalue=0, font=checkBoxFont)
        bikeCheckBox.grid(column=1, row=7, sticky=W, padx=5, pady=5)
        # pedestrian checkbox
        pedestrianCheckBox = tk.Checkbutton(checkBoxFrame, text="Pedestrian",
                                            variable=pedestrainCheckBoxBool, onvalue=1, offvalue=0, font=checkBoxFont)
        pedestrianCheckBox.grid(column=1, row=8, sticky=W, padx=5, pady=5)

    def init_video_canvas(self):
        videoLabelFont = font.Font(size=20)
        videoFrame = LabelFrame(self, text='Video Player', font=videoLabelFont)
        videoFrame.columnconfigure(1, weight=1)
        videoFrame.rowconfigure(1, weight=1)
        videoFrame.grid(column=1, row=1, columnspan=8, rowspan=12, sticky=E+W+S+N, padx=20)
        imageCanvas = tk.Canvas(videoFrame, bg='#000000')
        imageCanvas.grid(column=1, row=1, sticky=E+W+S+N, padx=5, pady=5)

    def init_informations(self):
        informationFont = font.Font(size=18)
        buttonFrame = LabelFrame(self, text='Informations', font=informationFont)
        buttonFrame.grid(column=1, row=13, sticky=E+W+S+N, padx=20, pady=10)
        fileNameLabel = tk.Label(buttonFrame, text="File Name:", font=informationFont)
        fileNameLabel.grid(column=1, row=13, sticky=W, padx=16, pady=5)
        resolutionLabel = tk.Label(buttonFrame, text="Resolution:", font=informationFont)
        resolutionLabel.grid(column=2, row=13, sticky=W, padx=16, pady=5)
        sizeLabel = tk.Label(buttonFrame, text="Size:", font=informationFont)
        sizeLabel.grid(column=3, row=13, sticky=W, padx=16, pady=5)
        durationLabel = tk.Label(buttonFrame, text="Duration:", font=informationFont)
        durationLabel.grid(column=4, row=13, sticky=W, padx=16, pady=5)
        frameRateLabel = tk.Label(buttonFrame, text="Frame Rate:", font=informationFont)
        frameRateLabel.grid(column=5, row=13, sticky=W, padx=16, pady=5)
        inOutDistanceLabel = tk.Label(buttonFrame, text="In-Out Distance:", font=informationFont)
        inOutDistanceLabel.grid(column=6, row=13, sticky=E, pady=5)
        inOutDistance = tk.Text(buttonFrame, height=1, width=10, font=informationFont, spacing1=4)
        inOutDistance.grid(column=7, row=13, padx=5, sticky=E+W+S+N)


def gui_init():
    root = tk.Tk()
    root.geometry("1800x1200")
    window = Main_Window()
    root.mainloop()
