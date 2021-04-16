from dearpygui.core import *
from dearpygui.simple import *
import cv2
import numpy as np


with window("main_window"):

    with menu_bar("Main Menu Bar"):

        with menu("Load Data"):
            add_menu_item("Load Video")
            add_menu_item("Load ROI and Process Lines")
            add_menu_item("Load In-Out Lines")

        with menu("Stabalization"):
            add_menu_item("Video Stabalization (Cross)")
            add_menu_item("Video Stabalization All (Cross)")
            add_menu_item("Video Stabalization (Full)")
            add_menu_item("Video Stabalization All (Full)")

        with menu("Data Extraction"):
            add_menu_item("Trajectory Data Extraction (Full)")
            add_menu_item("Trajectory Data Extraction (Cross)")
            add_menu_item("Trajectoty Data Extraction (Moto)")

        with menu("Dectetion"):
            add_menu_item("Vehicle Detection (Faster-RCNN)")
            add_menu_item("Motor Detection (YOLO)")

        with menu("Output Infromation"):
            add_menu_item("Fill up In-Out informations")
            add_menu_item("Output Replay Video")
            add_menu_item("Output Replay Video with In-Out Lines")

        add_menu_item("Help")
     
    add_checkbox( "Sedan", default_value = False )
    add_checkbox( "Truck", default_value = False )
    add_checkbox( "Bus", default_value = False )
    add_checkbox( "Trailer Head", default_value = False )
    add_checkbox( "Cargo", default_value = False )
    add_checkbox( "Moto", default_value = False )
    add_checkbox( "Bike", default_value = False )
    add_checkbox( "Pedestrain", default_value = False )
 
    # tkinter
    root = Tk()
    root.title("A simple GUI")
    root.button = Button(root, text="Press me")
    root.button.pack()


start_dearpygui(primary_window="main_window")