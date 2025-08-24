from tkinter import *
from tkinter import ttk

import math

def calculate(*args):
    try:
        value = float(degree.get())
        radians.set(float(value*(math.pi/180)))
    except ValueError:
        pass

root = Tk()
root.title("deg to rad")

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 100)
root.rowconfigure(0, weight = 100)

degree = StringVar()
degree_entry = ttk.Entry(mainframe, width = 7, textvariable = degree)
degree_entry.grid(column = 2, row = 1, sticky = (W, E))

radians = StringVar()
ttk.Label(mainframe, textvariable = radians).grid(column = 2, row = 2, sticky = (W, E))

ttk.Button(mainframe, text = "Convert", command = calculate).grid(column = 3, row = 3, sticky = W)
ttk.Label(mainframe, text = "degrees").grid(column = 3, row = 1, sticky = W)
ttk.Label(mainframe, text = "is equivalent to").grid(column = 1, row = 2, sticky = E)
ttk.Label(mainframe, text = "radians").grid(column = 3, row = 2, sticky = W)

for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

degree_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()




