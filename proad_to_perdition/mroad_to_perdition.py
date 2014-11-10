__author__ = 'Mr.101Freaking'
from tkinter import *
import json

root = Tk()


######### PROGRAM ##########################################################################

#--------------- READ .JSON ----------------------------------------------------------------

with open('droad_to_perdition.json') as json_data :
    data = json.load(json_data)
    json_data.close()

print (data)



######### LAYOUT ###########################################################################


#---------------- FRAME --------------------------------------------------------------------
frame = Frame(root, width=750, height=500)
frame.grid()


#---------------- BUTTONS ------------------------------------------------------------------















root.mainloop()