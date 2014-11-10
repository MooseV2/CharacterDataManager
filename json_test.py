
import json
import Tkinter as tk

root = tk.Tk()

with open('data.json') as json_data:
    data = json.load(json_data)
    json_data.close()
.....
print data


'''
for faction in data:
    print "Faction: ", faction
    for countries in data[faction]:
        print "->\tCountry", countries
        for units in data[faction][countries]:
            print units
            for unitinfo in data[faction][countries][units]:
                print "->\t->\t", unitinfo, "\t:\t", data[faction][countries][units][unitinfo]'''


def hello():
    print "hello!"

menubar = tk.Menu(root)

# create a pulldown menu, and add it to the menu bar
for faction in data:
    menu = tk.Menu(menubar, tearoff=0)


# display the menu
root.config(menu=menubar)

root.mainloop()