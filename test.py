from tkinter import *

def SedanChecked():
    if sedan_val.get() == 1:
        print('Sedan on')
    elif sedan_val.get() == 0:
        print('Sedan off')
def BusChecked():
    if bus_val.get() == 1:
        print('bus on')
    elif bus_val.get() == 0:
        print('bus off')
def TruckChecked():
    if truck_val.get() == 1:
        print('truck on')
    elif truck_val.get() == 0:
        print('truck off')
def TrailerHeadChecked():
    if trialerHead_val.get() == 1:
        print('trialerHead on')
    elif trialerHead_val.get() == 0:
        print('trialerHead off')
def CargoChecked():
    if cargo_val.get() == 1:
        print('cargo on')
    elif cargo_val.get() == 0:
        print('cargo off')
def MotoChecked():
    if moto_val.get() == 1:
        print('moto on')
    elif moto_val.get() == 0:
        print('moto off')
def BikeChecked():
    if bike_val.get() == 1:
        print('bike on')
    elif bike_val.get() == 0:
        print('bike off' )
def PedestrainChecked():
    if pedestrain_val.get() == 1:
        print('pesdestrain on')
    elif pedestrain_val.get() == 0:
        print('pesdestrain off')

sedan_val = IntVar()
truck_val = IntVar()
bus_val = IntVar()
trialerHead_val = IntVar()
cargo_val = IntVar()
moto_val = IntVar()
bike_val = IntVar()
pedestrain_val = IntVar()

Checkbutton(ws, text="Sedan", variable = sedan_val, onvalue=1, offvalue=0, command=SedanChecked).pack()
Checkbutton(ws, text="Truck",  variable = truck_val, onvalue=1, offvalue=0, command=TruckChecked).pack()
Checkbutton(ws, text="Bus", variable = bus_val, onvalue=1, offvalue=0, command=BusChecked).pack()
Checkbutton(ws, text="Trialer Head", variable = trialerHead_val, onvalue=1, offvalue=0, command=TrailerHeadChecked).pack()
Checkbutton(ws, text="Cargo", variable = cargo_val, onvalue=1, offvalue=0, command=CargoChecked).pack()
Checkbutton(ws, text="Moto", variable = moto_val, onvalue=1, offvalue=0, command=MotoChecked).pack()
Checkbutton(ws, text="Bike", variable = bike_val, onvalue=1, offvalue=0, command=BikeChecked).pack()
Checkbutton(ws, text="Pedestrian", variable = pedestrain_val, onvalue=1, offvalue=0, command=PedestrainChecked).pack()

ws = Tk()
ws.title('Interface')
ws.geometry('200x500')
ws.mainloop()