from tkinter import *
from tkinter import ttk

import linear_graphs_functions as lgf

root = Tk()
root.title("Random Graph Generator")
mainframe = ttk.Frame(root, padding = 10)
mainframe.grid()

x_axis = []
y_axis = []

ttk.Button(mainframe, text = "Generate x and y values", command = lgf.random_xy_values(x_axis, y_axis, 1, 1, 10)).grid(row = 0, column = 0)
ttk.Button(mainframe, text = "Show Graph", command = lgf.generate_graph(x_axis, y_axis)).grid(row = 1, column = 0)
ttk.Button(mainframe, text = "Quit", command = root.destroy).grid(row = 2, column = 0)
ttk.Button(mainframe, text = "Clear Data").grid(row = 3, column = 0)

root.mainloop()