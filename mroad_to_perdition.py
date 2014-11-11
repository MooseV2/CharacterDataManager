__author__ = 'Mr.101Freaking'
from tkinter import *
import json
from widget_handler import *

root = Tk()


######### PROGRAM ##########################################################################

#--------------- READ .JSON ----------------------------------------------------------------

with open('droad_to_perdition.json') as json_data :
    data = json.load(json_data)
    json_data.close()

print (data["Demons"]["O'fra"]["Undead Viking"])



######### LAYOUT ###########################################################################


#---------------- FRAME --------------------------------------------------------------------
frame = Frame(root, width=750, height=500)
frame.grid()

#---------------- DROPLISTS ----------------------------------------------------------------
selectedf = StringVar(frame)
selectedf.set("Republic")

fractions = []
for fraction in data :
    fractions.append(fraction)
fractions.sort()

dlistf = OptionMenu(frame, selectedf, *fractions)
dlistf.grid(row=0, column=0)

selectedc = StringVar(frame)

countries = []
for country in data[selectedf.get()] :
    countries.append(country)
countries.sort()

selectedc.set(countries[0])

dlistc = OptionMenu(frame, selectedc, *countries)
dlistc.grid(row=0, column=1)

selectedu = StringVar(frame)

units = []
for unit in data[selectedf.get()][selectedc.get()] :
    units.append(unit)
units.sort()

selectedu.set(units[0])

dlistu = OptionMenu(frame, selectedu, *units)
dlistu.grid(row=0, column=2)

#---------------- BUTTONS ------------------------------------------------------------------
bPower = DataEntry(frame, label='Power', min_value=0, max_value=10)
bPower.grid(row=2 , column=0)

bPrecision = DataEntry(frame, label='Precision', min_value=0, max_value=10)
bPrecision.grid(row=2 , column=1)

bStrenght = DataEntry(frame, label='Strength', min_value=0, max_value=10)
bStrenght.grid(row=2 , column=2)

bDefence = DataEntry(frame, label='Defence', min_value=0, max_value=10)
bDefence.grid(row=2 , column=3)

bAttacks = DataEntry(frame, label='Attacks', min_value=0, max_value=10)
bAttacks.grid(row=2 , column=4)

bLives = DataEntry(frame, label='Lives', min_value=0, max_value=10)
bLives.grid(row=2 , column=5)

bBravery = DataEntry(frame, label='Bravery', min_value=0, max_value=10)
bBravery.grid(row=2 , column=6)

lista = ["None", "Simple", "Heavy", "Massive"]

bArmor = DataString(frame, lista, label='Armor')
bArmor.grid(row=2 , column=7)

bbPoints = DataEntry(frame, label='Basic Points', min_value=0, max_value=1000)
bbPoints.grid(row=2 , column=8)

#---------------- LIVE UPDATE / LOADING SINGLE UNITS ----------------------------------------------------------------
def callbackf() :

    selectedc = StringVar(frame)

    countries = []
    for country in data[selectedf.get()] :
        countries.append(country)
    countries.sort()

    selectedc.set(countries[0])

    dlistc = []
    dlistc.append(countries)

    dlistu = []

def callbackc() :

    selectedu = StringVar()

    units = []
    for unit in data[selectedf.get()][selectedc.get()] :
        units.append(unit)
    units.sort()

    selectedu.set(units[0])

    dlistu = []
    dlistu.append(units)

def callbacku() :
    bPower.change_value(data[selectedf.get()][selectedc.get()][selectedu.get()]["Power"])
    bPrecision.change_value(data[selectedf.get()][selectedc.get()][selectedu.get()]["Precision"])
    bStrenght.change_value(data[selectedf.get()][selectedc.get()][selectedu.get()]["Strength"])
    bDefence.change_value(data[selectedf.get()][selectedc.get()][selectedu.get()]["Defence"])
    bAttacks.change_value(data[selectedf.get()][selectedc.get()][selectedu.get()]["Attacks"])
    bLives.change_value(data[selectedf.get()][selectedc.get()][selectedu.get()]["Lives"])
    bBravery.change_value(data[selectedf.get()][selectedc.get()][selectedu.get()]["Bravery"])
    bArmor.change_value(data[selectedf.get()][selectedc.get()][selectedu.get()]["Armor"])
    bbPoints.change_value(data[selectedf.get()][selectedc.get()][selectedu.get()]["bPoints"])



selectedf.trace("w", callbackf())
selectedc.trace("w", callbackc())
selectedu.trace("w", callbacku())














root.mainloop()