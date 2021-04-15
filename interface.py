from dearpygui.core import *
from dearpygui.simple import *

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

start_dearpygui(primary_window="main_window")
