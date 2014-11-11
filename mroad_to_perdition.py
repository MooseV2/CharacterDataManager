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

listf = OptionMenu(frame, selectedf, *fractions)
listf.grid(row=0, column=0)

selectedc = StringVar(frame)

countries = []
for country in data[selectedf.get()] :
    countries.append(country)
countries.sort()

selectedc.set(countries[0])

listc = OptionMenu(frame, selectedc, *countries)
listc.grid(row=0, column=1)

selectedu = StringVar(frame)

units = []
for unit in data[selectedf.get()][selectedc.get()] :
    units.append(unit)
units.sort()

selectedu.set(units[0])

listu = OptionMenu(frame, selectedu, *units)
listu.grid(row=0, column=2)

#---------------- LIVE UPDATE ----------------------------------------------------------------

def callbackf() :

    selectedc = StringVar(frame)
    selectedc.set(" ")

    countries = []
    for country in data[selectedf.get()] :
        countries.append(country)
    countries.sort()

    listc = []
    listc.append(countries)

    listu = []

def callbackc() :

    selectedu = StringVar()
    selectedu.set(" ")

    units = []
    for unit in data[selectedf.get()][selectedc.get()] :
        units.append(unit)
    units.sort()

    listu = []
    listu.append(units)

#def callbacku() :


selectedf.trace("w", callbackf())
selectedc.trace("w", callbackc())




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

bArmor = DataEntry(frame, label='Armor', min_value=0, max_value=3)
bArmor.grid(row=2 , column=7)
bArmor

bPoints = DataEntry(frame, label='Points', min_value=0, max_value=1000)
bPoints.grid(row=2 , column=8)











root.mainloop()