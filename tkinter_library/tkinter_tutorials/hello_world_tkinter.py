from tkinter import *
from tkinter import ttk

root = Tk()
mainframe = ttk.Frame(root, padding = 20)
mainframe.grid()
ttk.Label(mainframe, text = "Hello World").grid(column = 0, row = 0)
ttk.Button(mainframe, text = "Quit", command = root.destroy).grid(column = 1, row =0)

root.mainloop()

