#Widgets file
#Anthony DeSouza

import tkinter as tk

class DataEntry(tk.Frame):
    def __init__(self, master, label='', value=0, min_value=None, max_value=None):
        #Attributes
        self.value = value
        self.name = label
        self.min_value = min_value
        self.max_value = max_value

        tk.Frame.__init__(self, master)
        self.master = master

        self.name_var = tk.StringVar(self, value=self.name)
        self.name_label = tk.Label(self, textvariable=self.name_var)
        self.name_label.grid(row=0, columnspan=3)

        self.button_plus = tk.Button(self, text="+", command=self.increase_value)
        self.button_plus.grid(row=1, column=2)

        self.button_minus = tk.Button(self, text="-", command=self.decrease_value)
        self.button_minus.grid(row=1, column=0)

        self.value_var = tk.IntVar(self, value=self.value)
        self.value_var.trace("w", self.change_entry)
        self.value_box = tk.Entry(self, textvariable=self.value_var, justify=tk.CENTER, width=4)
        self.value_box.grid(row=1, column=1)

    def change_entry(self, *args):
        try:
            text_value = self.value_var.get()
            self.value = text_value
        except ValueError:
            pass

    def change_value(self, new_value=0):
        self.value = new_value
        if (self.max_value != None):
            self.value = min(self.value, self.max_value)
        if (self.min_value != None):
            self.value = max(self.value, self.min_value)
        self.value_var.set(self.value)

    def increase_value(self, amount=1):
        self.change_value(self.value + amount)

    def decrease_value(self, amount=1):
        self.change_value(self.value - amount)

    def set_label(self, label):
        self.name = label
        self.name_var.set(label)


class DataString(tk.Frame):
    def __init__(self, master, list, label='', value=0):
        #Attributes
        self.value = value
        self.name = label
        self.list = list
        self.min_value = 0
        self.max_value = len(list) - 1

        tk.Frame.__init__(self, master)
        self.master = master

        self.name_var = tk.StringVar(self, value=self.name)
        self.name_label = tk.Label(self, textvariable=self.name_var)
        self.name_label.grid(row=0, columnspan=3)

        self.button_plus = tk.Button(self, text="+", command=self.increase_value)
        self.button_plus.grid(row=1, column=2)

        self.button_minus = tk.Button(self, text="-", command=self.decrease_value)
        self.button_minus.grid(row=1, column=0)

        self.value_var = tk.StringVar(self, value=self.list[self.value])
        self.value_var.trace("w", self.change_entry)
        self.value_box = tk.Entry(self, textvariable=self.value_var, justify=tk.CENTER, width=20)
        self.value_box.grid(row=1, column=1)

    def change_entry(self, *args):
        try:
            text_value = self.value_var.get()
            self.value = self.list.index(text_value)
        except ValueError:
            pass

    def change_value(self, new_value=0):
        self.value = new_value
        if (self.max_value != None):
            self.value = min(self.value, self.max_value)
        if (self.min_value != None):
            self.value = max(self.value, self.min_value)
        self.value_var.set(self.list[self.value])

    def increase_value(self, amount=1):
        self.change_value(self.value + amount)

    def decrease_value(self, amount=1):
        self.change_value(self.value - amount)

    def set_label(self, label):
        self.name = label
        self.name_var.set(label)


